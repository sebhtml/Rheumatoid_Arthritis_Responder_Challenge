REST API: http://hud.rel.rest.doc.sagebase.org.s3-website-us-east-1.amazonaws.com/

To get my API key: https://repo-prod.prod.sagebase.org/auth/v1/secretKey (does not work)

Python API: http://python-docs.synapse.org/

There is a $HOME/.synapseConfig, but I did not find the documentation.

The command synapse login --help (and the command synapse in general) is not secure on
multi-users server because the -p parameter is the password and is visible with
'ps aux'.

I will therefore use the Python API.
