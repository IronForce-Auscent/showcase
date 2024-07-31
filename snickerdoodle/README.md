# snickerdoodle

**Creator - Solitude**

*Category - Web*

*Difficulty - Easy*

## Description
I love snickerdoodles

## Hints (Optional)

## Setup Guide (Optional)
<!--
Only applicable if challenge requires server hosting.

All setup files should be placed in service folder.
-->
1. cd snickerdoodle/snickerdoodle/src
2. docker run --tag snickerdoodles-prod .
3. docker images (optional, to verify that container is ready)
4. docker run -d -p 5000 snickerdoodles-prod
5. docker ps (optional, to verify that container is running)

## Distribution (Optional)
<!--
Only applicable if you need participants to download file(s).

All files should be placed in distrib folder.
-->

## Solution
<!--
Please make it descriptive enough, don't need to challenge the challenge vetter D:
-->
Solution to this challenge
1. Enter a random value to get a cookie
2. Inspect the newly generated cookie named "cookie"
3. Decode the payload
4. Modify the "is_admin" value to True
5. Guess the secret key is "snickerdoodle" (May consider releasing as hint if it turns out to be too difficult to guess)
6. Replace "cookie" payload with new payload and refresh page

## Video Solution (Optional)

## Flag
`"NYP{1_l0v3_sn1ck3rd00dl3s!}"`

## Recommended Reads (Optional)
https://token.dev OR https://jwt.io
