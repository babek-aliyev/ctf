# Bandit Level 21 =>Level 22 | OverTheWire

## Description
A program is running automatically at regular intervals from cron, the time-based job scheduler. Look in /etc/cron.d/ for the configuration and see what command is being executed.

## Analysis
To start analyzing this `bandit21` machine we can use information that we got from description of this lab. First thing I did was changing directory to `/etc/cron.d/`. In this directory we can observe the following files:
```bash
bandit21@bandit:/etc/cron.d$ ls
behemoth4_cleanup  cronjob_bandit23  leviathan5_cleanup    sysstat
clean_tmp          cronjob_bandit24  manpage3_resetpw_job
cronjob_bandit22   e2scrub_all       otw-tmp-dir
```

As you can see we have got several `.sh` cron files.

## Solution
To solve this problem first we need to execute `cronjob_bandit22`:
```bash
bandit21@bandit:/etc/cron.d$ cronjob_bandit22.sh 
chmod: changing permissions of '/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv': Operation not permitted
/usr/bin/cronjob_bandit22.sh: line 3: /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv: Permission denied
```

As you can see we couldn't do it because of permission constraints. However, we got something interesting: `/tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv`. We cannot change directory to `/tmp/` to list it content, however, we can read this file:
```bash
bandit21@bandit:/etc/cron.d$ cat /tmp/t7O6lds9S0RqQh9aMcz6ShpAoZKF7fgv
tRae0UfB9v0UzbCdn9cY0gQnds9GF58Q
```

This is how we solve this ctf!
