# How to

## Client Side Setup

- 1. Background

A GPG key is identified by a 8-letter string
locally ($GPGKEY) and by email address when
talking between two parties.

- 2. Setup GPG

```
gpg --generate-key
```

- 3. Send public key to server

```
gpg --output - --export -a $GPGKEY
```

- 4. Set up GBS script

Put gbs script to working directory;
edit it to setup the RECIPIENT and URL.
RECIPIENT is the email ID.


# Server Side Setup

- 1. Clone the project

- 2. Update config.py

```
PROJECT=project_name
```

- 3. Import public key

```
gpg --import <pub_key_file>
gpg --edit-key <recient@email> trust
```



