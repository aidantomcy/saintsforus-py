# Saints for Us

This is a website about a few saints. This is a personal project that I began because there are not  
many websites on this topic. This project uses the Flask framework for the backend and I have  
used plain HTML, CSS and JavaScript.

## Content and Styling

I have used Bootstrap for some of the styles.  
I have made some mistakes with the numbering for each saint in commit messages.  
The views.py contains the route for the home page and the other main pages,  
while the pages.py contains the routes for all the saints.  
I will probably dockerize this application later on.  
This Website will be deployed soon.

## Running Locally
1. Create a .env file in the website directory with the following keys:  
   * SECRET_KEY: A secret key for the application.
   * EMAIL_SENDER: An email id to send a mail in the contact form page.
   * EMAIL_PASSWORD: The password for the email sender.
   * EMAIL_RECEIVER: A receiver email to get the mail sent by the email sender.
2. Run the server:  
   ```
   $ python main.py
   ```
3. Open your browser and head to `http://localhost:5000`


## Contact
If you have any feedback, comments or criticism, please mail your contents to info.saintsforus@gmail.com

## Inspiration
Some inspiration to make this website came from [miracolieucaristici.org](http://www.miracolieucaristici.org/)

## Pictures

<p align="center">
    <img src="img1.png">
    <br>
    <br>
    <img src="img2.png">
</p>
