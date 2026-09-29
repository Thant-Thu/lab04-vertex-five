# lab04-vortex_five

## Who Did What
| File | Name | Student ID | Commits |
|---|---|---|---|
| test_deposit.py | Khant Naing Hein | 6805140019 | 2 |
| test_withdraw.py | Zaw Moe Aung | 6805140020 | 3 |
| test_teardown.py | Lynn Thant Maung | 6805140001 | 1 |
| test_shared.py | Than Sin Hein | 6805140004 | 2 |
| conftest.py | Thant Thurein Lynn | 6805140024 | 3 |
| .gitignore & bank.py (repo setup) | Thant Thurein Lynn | 6805140024 | (included above) |

## Our Merge Conflict

While working on the "Who Did What" table in README.md, two team members pushed changes to the same section at nearly the same time. When the second push was rejected, running `git pull` produced a conflict:

```text
<<<<<<< HEAD
| test_teardown.py | Lynn Thant Maung | 6805140001 | |
=======
| test_shared.py | Than Sin Hein | 6805140004 | |
>>>>>>> origin/main
```

We opened README.md, removed the conflict markers, and kept both rows since each one recorded a different member's contribution. After the table was clean, we staged the file with `git add README.md`, committed with a message describing the resolution, and pushed successfully.

Git could not resolve this automatically because both the local and remote branches had edited the exact same lines in the same file. Git has no way to know whether one version should be discarded, kept, or merged with the other, so it stopped and asked us to decide manually.

## Git Contribution Summary
```
    3  Thant-Thu
    3  Zaw Moe Aung - Zak
    3  louis40004
    2  Thant Sin Hein - Louis
    2  khant2905
    1  Voldiel
```
Note: louis40004 and Thant Sin Hein - Louis are the same team member (Than Sin Hein), shown under two names because of a Git configuration mismatch across his computer and account.

## Reflection Questions
Answer each question in one or two sentences:

1. **Why was your push rejected, and how did you fix it?**
Our push was rejected because a teammate had already pushed commits to the remote repository that we didn't have locally. We fixed it by running `git pull` to bring in their changes before pushing ours again.

2. **Why could Git not resolve the README conflict automatically?**
Git could not resolve it automatically because two team members edited the same lines of README.md at the same time. Git cannot decide on its own which version is correct or whether both should be kept, so it marks the section with `<<<<<<<`, `=======`, and `>>>>>>>` and leaves the decision to us.

3. **What is the difference between committing and pushing?**
Committing saves a snapshot of changes to the local repository on our own computer. Pushing uploads those local commits to GitHub so the rest of the team can see and access them.

4. **How do fixtures reduce duplicated setup code in tests?**
Fixtures let us define reusable setup logic, like creating a `BankAccount` object, once in a single function. Tests that need that object just take it as a parameter instead of rewriting the same setup code each time.
