# Notes for Claude

## Pushing to GitHub

- Push directly to `master`. **No pull request is needed.**
- Pushes only work as the GitHub user **`christopherl-git`**. If the active `gh` CLI user is `chris-leigh-workerbee`, the push fails with a 403 permission error. Check with `gh auth status`, and if needed switch first:

  ```bash
  gh auth switch --user christopherl-git
  ```

- Git's saved Windows login may still be the other account. If a plain `git push origin master` still returns 403 after switching, either run `gh auth setup-git` once or push with a one-time credential helper:

  ```bash
  git -c credential.helper= -c 'credential.helper=!gh auth git-credential' push origin master
  ```
