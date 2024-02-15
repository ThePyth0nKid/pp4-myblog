[Back to README](https://github.com/ThePyth0nKid/pp4-myblog/blob/main/README.md)

---

## Testing Catalouge

<li><a href="#user-stories">User Stories Testing</a></li>
<ul>
<li><a href="#one">User Authentication</a></li>
<li><a href="#two">Responsive Design</a></li>
<li><a href="#three">View Paginated List of Posts</a></li>
<li><a href="#four">Read Blog Post</a></li>
<li><a href="#five">Commenting System</a></li>
<li><a href="#six">Comment Editing and Deletion</a></li>
<li><a href="#seven">Create Blog Post</a></li>
<li><a href="#eight">Update Blog Pos</a></li>
<li><a href="#nine">Delete Blog Post</a></li>
<li><a href="#ten">Upload Images to Blog Post</a></li>
<li><a href="#eleven">Admin Dashboard for Viewing Contact Messages</a></li>
</ul>
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

## Base Stories Testing

<h3 id="one">As a user, I can register for an account so that I can have a personalized experience on the blog platform.</h3>
Acceptance Criteria 1: The registration page should ask for a unique username and password.

Acceptance Criteria 2: Upon successful registration, I should receive a confirmation.

Acceptance Criteria 3: I should be able to log in with my registered credentials.

Test result:

<h3 id="two">As a user, I want the blog website to be accessible and user-friendly on various devices so that I can enjoy a seamless experience regardless of the device I'm using.</h3>
Acceptance Criteria 1: The website should adjust its layout and design based on the device's screen size.

Acceptance Criteria 2: Navigation and content should be clear and easy to interact with on desktop, tablet, and mobile.

Test result:

## Reader Stories Testing

<h3 id="three"></h3>As a reader I can view a paginated list of blog posts so that I can easily navigate through the content and explore multiple posts without overwhelming scrolling.
Acceptance Criteria 1: On the main blog page or a designated blog section, there should be a list of blog posts.

Acceptance Criteria 2: The list should be divided into pages, with a specific number of posts displayed per page.

Acceptance Criteria 3: Each page should include clear navigation options, such as "Previous" and "Next" buttons, to move between pages.

Acceptance Criteria 4: The current page number or position within the paginated list should be displayed for reference.

Acceptance Criteria 5: Clicking on a blog post title or preview should take me to the full content of that post.

Acceptance Criteria 6: If there are more posts than can fit on a single page, the platform should automatically generate and display additional pages.

Acceptance Criteria 7: The pagination system should ensure that the list remains organized and user-friendly, even as new posts are added to the platform.

Test result:

<h3 id="four">As a reader, I can view blog posts so that I can stay informed about the blogger's content.</h3>
Acceptance Criteria 1: On the main blog page, there should be a list of all published blog posts.

Acceptance Criteria 2: Clicking on a post title should take me to a page displaying the full content of that post.

Acceptance Criteria 3: Each blog post should show the publication date.

<h3 id="five">As a reader, I can leave comments on blog posts so that I can share my thoughts and engage with the content.</h3>
Acceptance Criteria 1: I can share my thoughts and engage with the content.

Acceptance Criteria 2: I should be able to enter my comment and submit it.

Acceptance Criteria 3: Comments should be displayed on the post.

Test result:

<h3 id="six">As a registered user I can edit and delete my comments so that can correct mistakes or remove outdated information.</h3>
Acceptance Criteria 1: When I view a comment I've posted, I see an "Edit" button next to it.

Acceptance Criteria 2: When I click the "Edit" button, I can make changes to the content of my comment.

Acceptance Criteria 3: After editing, I can save my changes, and the comment will be updated with the new content.

Acceptance Criteria 4: I can only edit my own comments and not those made by other users.

Acceptance Criteria 5: When I view a comment I've posted, I also see a "Delete" button next to it.

Acceptance Criteria 6: When I click the "Delete" button, I am prompted to confirm the deletion.

Acceptance Criteria 7: After confirming the deletion, the comment is removed from the system and no longer visible to other users.

Acceptance Criteria 8: I can only delete my own comments and not those made by other users.

Test result:

## Blogger Stories Testing

<h3 id="seven">As a blogger I can create a new blog post so that I can share my thoughts and experiences with my audience.</h3>
Acceptance Criteria 1: When I log in to the blog platform, I should see a "Create New Post" button.

Acceptance Criteria 2: The create post page should include fields for the title, content, and any relevant metadata.

Acceptance Criteria 3: After submitting the new post, it should be immediately visible on the blog.

Test result:

<h3 id="eight">As a blogger, I can edit my existing blog posts so that I can keep my content up-to-date and accurate.</h3>
Acceptance Criteria 1: Each blog post should have an "Edit" option on the main blog page.

Acceptance Criteria 2: Clicking on the "Edit" option should take me to an edit page with the current content of the post.

Acceptance Criteria 3: After updating a post, the changes should be immediately reflected on the main blog page.

Test result:

<h3 id="nine">As a blogger, I can delete blog posts so that my blog remains organized and trustworthy.</h3>
Acceptance Criteria 1: Each blog post should have a "Delete" option on the main blog page.

Acceptance Criteria 2: Clicking on the "Delete" option should prompt me for confirmation before removing the post.

Acceptance Criteria 3: After deletion, the post should be removed from the main blog page.

<h3 id="ten">As a blogger I can enhance my blog posts with images so that I can visually engage and communicate with my audience.</h3>
Acceptance Criteria 1: On the blog post creation/edit page, there should be an option to upload images.

Acceptance Criteria 2: I should be able to select and upload one image from my local device.

Acceptance Criteria 3: The system should support common image formats such as JPEG, PNG, and GIF.

Acceptance Criteria 4: Uploaded images should be displayed within the blog post content.

Test result:

<h3 id="eleven">As a blogger I can access and view messages sent through the 'Contact Me' form so that I can efficiently manage and respond to user inquiries and feedback.</h3>
Acceptance Criteria 1: Ensure that there is a dedicated link in the navbar which is accessible only to admin and superuser accounts. This link should lead to a page or a section where messages from the 'Contact Me' form are listed.

Acceptance Criteria 2:On accessing the link, the admin/superuser should be presented with a list or table displaying the messages. This should include relevant details such as the sender's name, email and message content of the message submission.


Acceptance Criteria 3:Ensure that the message viewing functionality is secure and respects privacy. Only authorized admin or superusers should be able to view these messages.

Test result:

## User Stories (should and could) that are not done

As a user/reader I can bookmark or save my favorite blog posts so that can easily revisit and share them later.

As a user I can sign in to the blog platform using my Google account so that I can access the platform with minimal effort and use my existing Google credentials.

As a visitor to the website I can view the 'About Me' page so that I can learn more about the website owner, their background, interests, and professional journey.

---

<h2 id="manual-testing">Manual Testing</h2>

### General

<h3 id="navigation">Navigation Bar</h3>

* All links correctly redirect to the correct pages for visitors.
* Navbar is fully responsive on small/medium/large devices.
* Reader sees correct link "Contact Me" when logged in.
* Blogger sees correct links "Messages" and "Create Post" when logged in.
* Navbar collapse works on smaller devices.


<h3 id="footer">Footer</h3>

* All icon links work correctly.
* All links open in a new pag
* The footer appears at the end of the page.

<h3 id="homepage">Homepage</h3>

* All buttons work and links correctly.
* Icons are being displayed correctly.
* Images are displayed correctly.
* Good contrast between text/images/buttons.

<h3 id="signup">Signup page</h3>

* Username and password are required as expected.
* Email are optional.
* After a successful login, a confirmation message is displayed: "Successfully signed in as ..."
* The username cannot be assigned twice, and if one tries to register with a username that is already in use, a message will be displayed after the registration attempt: "A user with that username already exists."
* The password confirmation works correctly and shows a message when two different passwords are entered: "You must type the same password each time."
* The system also correctly identifies and notifies when a password is entirely numeric, displaying the message: "This password is entirely numeric."
* The system checks for passwords that are too similar to the user's other personal information and displays the message: "Your password can’t be too similar to your other personal information."
* The system requires passwords to have a minimum length and displays the message: "Your password must contain at least 8 characters."
* The system checks for commonly used passwords and will display the message: "Your password can’t be a commonly used password" if such a password is attempted.

<h3 id="signout">Signout page</h3>

* Upon attempting to sign out, the system will prompt with the message: "Are you sure you want to sign out?"
* After signing out, the system displays the message: "You have signed out."

<h3 id="login">Login page</h3>

* Form works as expected with username and password.
* After a successful login, a confirmation message is displayed: "Successfully signed in as nelson-mehlis."

### Reader

<h3 id="post-detail-reader">Post Detail Reader</h3>

* As a reader, you can write comments on the post detail page.
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

* .

* 

<h3 id="responsivness">Responsivness</h3>

Chrome dev tools were used throughout the development of the project to test responsiveness. Responsiveness was tested using Dev Tools to emulate the following devices.

* iPhone SE
* iPhone XR
* iPhone 12 Pro
* iPhone 14 Pro Max
* Pixel 7
* Samsung Galaxy S8+
* Samsung Galaxy S20 Ultra
* iPad Mini
* iPad Air
* iPad Pro
* Surface Pro 7
* Surface Duo
* Galaxy Fold
* Samsung Galaxy A51/71

<h3 id="browser-testing">Browser Testing</h3>

During development, testing was mainly done solely using Google Chrome.

In production the site has been tested on the following browsers.

* Firefox
* Safari
* Opera

---

<h2 id="validation">Validation</h2>

### [W3C HTML Validator](https://validator.w3.org/)

#### Check by address

* 0 Errors
* 0 Warnings

#### Check by text input

* 8 Errors
* 0 Warnings

When testing through text input with the W3C HTML validator, there were 8 error messages, all stemming from the Summernote widget. In the current phase, these could only be accepted and not debugged. However, all functionalities are still operational.

### [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

* 0 Errors
* 0 Warnings

### [JSHint Javascript Validator](https://jshint.com/)

* 0 Errors
* 11 Warnings

During code testing, a total of 11 warnings related to the use of ES6-specific features such as const for variable declarations, arrow functions (=>), and template literals were observed. These warnings are not indicative of incorrect or unexpected code; instead, they reflect adherence to modern JavaScript practices compliant with the ECMAScript 6 (ES6) standard.

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
