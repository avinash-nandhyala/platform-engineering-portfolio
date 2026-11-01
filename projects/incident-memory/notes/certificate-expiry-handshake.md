# SAMPLE — SSL handshake errors

Symptom: SSL handshake errors for one hostname, other hostnames fine.
Root cause (generic pattern): certificate for that hostname had expired / was not rotated in the gateway secret.
Fix: rotate the certificate, update the gateway secret reference, verify with a fresh client connection.
Lesson: track certificate expiry per hostname, not just per cluster, and alert before expiry.
