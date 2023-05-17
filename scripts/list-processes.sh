# This command works by changing the grep pattern so it doesn't match itself.
# When grep searches for the pattern '[m]onk', it matches any process that contains
# 'monk'. But when it looks at its own command line in the process list, it sees
# '[m]onk' which doesn't match the pattern, so it doesn't include itself in the output.
# The second grep excludes list-processes itself, because it is run using monk
ps aux | grep '[m]onk' | grep -v 'list-processes'

