FROM busybox
ENTRYPOINT /bin/true
# ruleid: multiple-entrypoint-instructions
ENTRYPOINT /bin/false
