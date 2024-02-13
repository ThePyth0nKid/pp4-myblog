[Back to README](https://github.com/ThePyth0nKid/pp4-myblog/blob/main/README.md)

---

## Testing Catalouge

<li><a href="#user-stories">User Stories Testing</a></li>
<li><a href="#manual-testing">Manual Testing</a></li>
<ul>
<li><a href="#navigation-bar">Navigation Bar</a></li>
<li><a href="#footer">Footer</a></li>
<li><a href="#homepage">Homepage</a></li>
<li><a href="#signup">Signup Page</a></li>
<li><a href="#login">Login Page</a></li>
<li><a href="#new-request">New Request Customer</a></li>
<li><a href="#request-overview">Request Overview</a></li>
<li><a href="#edit-request-customer">Edit Request Customer</a></li>
<li><a href="#delete-request-customer">Delete Request Customer</a></li>
<li><a href="#see-candidates">See Candidates as Customer</a></li>
<li><a href="#partner-overview">Partner Overview</a></li>
<li><a href="#send-candidate">Send Candidate</a></li>
<li><a href="#logout">Log out</a></li>
<li><a href="#adminpanel">Admin panel</a></li>
<li><a href="#authorization">Authorization</a></li>
<li><a href="#responsivness">Responsivness</a></li>
<li><a href="#browser-testing">Browser Testing</a></li>
</ul>
<li><a href="#validation">Validation</a></li>
<ul>
<li><a href="#validation">W3C HTML Validator</a></li>
<li><a href="#validation">W3C CSS Validator</a></li>
<li><a href="#validation">JSHint Javascript Validator</a></li>
<li><a href="#validation">PEP8 Python Validator</a></li>
</ul>
<li><a href="#lighthouse">Lighthouse Testing</a></li>
<li><a href="#bugs">Bugs</a></li>
<ul>
<li><a href="#solved-bugs">Solved Bugs</a></li>
</ul>

---

<h2 id="user-stories">User Stories Testing</h2>

---

## Reader Stories Testing

<h3 id="one">As a user, I can register for an account so that I can have a personalized experience on the blog platform.</h3>
Acceptance Criteria 1: The registration page should ask for a unique username and password.

Acceptance Criteria 2: Upon successful registration, I should receive a confirmation.

Acceptance Criteria 3: I should be able to log in with my registered credentials.

![signup](./readme-files/images/testing/1.png)
On the signup page, the user can sign up and add their own unique email and password.

<h3 id="two">As a reader, I can view blog posts so that I can stay informed about the blogger's content.</h3>
Acceptance Criteria 1: On the main blog page, there should be a list of all published blog posts.

Acceptance Criteria 2: Clicking on a post title should take me to a page displaying the full content of that post.

Acceptance Criteria : Each blog post should show the publication date.

![read-post](./readme-files/images/testing/2.png)
Click on the "Read More" button under a post title on the homepage to be redirected to a page where you can read the entire post.
<h3 id="three">As a reader, I can leave comments on blog posts so that I can share my thoughts and engage with the content.</h3>
Acceptance Criteria 1: I can share my thoughts and engage with the content.

Acceptance Criteria 2: I should be able to enter my comment and submit it.

Acceptance Criteria 3: Comments should be displayed on the post.

![commenting-sytem](./readme-files/images/testing/3.1.png)
If you're logged in as a user, leave a comment on the post page by clicking "Leave a Comment" under the text. Type your comment in the text field and click "Submit" to post your comment.

<h3 id="four">As a registered user I can edit and delete my comments so that can correct mistakes or remove outdated information.</h3>
Acceptance Criteria 1: When I view a comment I've posted, I see an "Edit" button next to it.

Acceptance Criteria 2: When I click the "Edit" button, I can make changes to the content of my comment.

Acceptance Criteria 3: After editing, I can save my changes, and the comment will be updated with the new content.

Acceptance Criteria 4: I can only edit my own comments and not those made by other users.

Acceptance Criteria 5: When I view a comment I've posted, I also see a "Delete" button next to it.

Acceptance Criteria 6: When I click the "Delete" button, I am prompted to confirm the deletion.

Acceptance Criteria 7: After confirming the deletion, the comment is removed from the system and no longer visible to other users.

Acceptance Criteria 8: I can only delete my own comments and not those made by other users.

![edit-delete-sytem](./readme-files/images/testing/3.1.png)

## Blogger Stories Testing



## User Stories (should and could) that are not done

As a user/reader I can bookmark or save my favorite blog posts so that can easily revisit and share them later.

As a user I can sign in to the blog platform using my Google account so that I can access the platform with minimal effort and use my existing Google credentials.

---

<h2 id="manual-testing">Manual Testing</h2>

### General

<h3 id="navigation">Navigation Bar</h3>

* 

<h3 id="footer">Footer</h3>

* 

<h3 id="homepage">Homepage</h3>

* 

<h3 id="signup">Signup page</h3>

* 

<h3 id="signout">Signout page</h3>

* 

<h3 id="login">Login page</h3>

### Reader

<h3 id="navigation-reader">Navigation Bar Reader</h3>

* 

<h3 id="post-detail-reader">Post Detail Reader</h3>

* 

<h3 id="contact-me">Contact Me</h3>

* 

### Blogger

<h3 id="navigation-blogger">Navigation Bar Blogger</h3>

* 

<h3 id="post-detail-blogger">Post Detail Blogger</h3>

* 

<h3 id="messages">Messages</h3>

* 

<h3 id="create-post">Create Post</h3>

* 

<h3 id="authorization">Authorization</h3>

This applies to every browser. User is authenticated in the browser when they log in.

* User gets redirected to login page if not authenticated for /new//order.

* Message 

<h3 id="responsivness">Responsivness</h3>

Chrome dev tools were used throughout the development of the project to test responsiveness. Responsiveness was tested using Dev Tools to emulate the following devices.

* Iphone 5
* Iphone 6/7/8
* Iphone 6/7/8 Plus
* Iphone X
* Ipad
* Ipad Pro

<h3 id="browser-testing">Browser Testing</h3>

During development, testing was mainly done solely using Google Chrome.

In production the site has been tested on the following browsers.

* Firefox
* Safari
* Opera

---

<h2 id="validation">Validation</h2>

### [W3C HTML Validator](https://validator.w3.org/)

* 0 Errors
* 0 Warnings


### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

* 0 Errors
* 0 Warnings

### [JSHint Javascript Validator](https://jshint.com/)

* 0 Errors
* 0 Warnings


### PEP8 Python Validator

* 0 Errors
* 0 Warnings

The python validator extension was used to test Python for Pep8 compliance with its built-in linting too.

* A lot of the Python errors were fixed during development.
Any errors related to files that were auto generated by Django were left untouched.
* Migration Files
* ./manage.py

<h3 id="lighthouse">Lighthouse Testing</h3>

#### On desktop for homepage

![lighthouse1]()

#### On mobile for homepage

![lighthouse1]()

---

<h2 id="bugs">Bugs</h2>


<h3 id="solved-bugs">Solved Bugs</h3>


---
