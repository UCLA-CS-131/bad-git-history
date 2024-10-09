# A (Bad) Git History

In general, a bad git history is one that does not show evidence of incremental development. For this example, the entire assignment is completed in one commit. 

There's no way to tell: 
- the order in which features were added
- what bugs were fixed along the way
- if any significant refactoring was done 

A good rule of thumb for a solid commit history addresses each of these points directly: **you should commit when you add a new feature, fix a bug, or perform any significant refactoring.**

You should also make sure your commit messages are **descriptive**. If you can't read your message and understand exactly what was changed, the message isn't descriptive enough.

Here's a descriptive message: `implement random line generator`

Here's a vague message (which you should avoid): `bug fix`

---

You can view the commit history by clicking the button above that looks like this:

![button](./commit-history-button.png)