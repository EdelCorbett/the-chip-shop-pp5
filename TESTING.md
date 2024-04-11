## Manual Testing
Browsers and Devices
* I have tested the site  on Chrome, Safari and Firefox
* I have tested the site on different screen sizes to confirm it is responsive mobile, Ipad and Desktop 
* I have tested all links to confirm they are functioning.

### Navigation Bar
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|  Home Button                 | Click      |  Redirects to home page                                            |    Pass   |
|  Menu                | Click      |  Opens to Menu page                                            |    Pass   |
|Contact Us                | Click      |  Opens Inquire form  page                                            |    Pass   |
|  My Account                | Click      |  Opens login and register links                                           |    Pass   |
|  Register                | Click      |  Opens | sign up form page                                            |    Pass   |
|  Login                 | Click      |  Opens sign in form page                                            |    Pass   |
|  Bascket               | Click      |  Opens | basket page      

### Footer 
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|  Instagram icon     | Click      |  opens Instagram                                                  |    Pass   |
|  Facebook icon     | Click      |  opens Facebook                                                 |    Pass   |
|  TicToc icon     | Click      |  opens Tictoc         |Pass
|  Mail Chip     | enter email      |  Subscribes to newletter     |Pass
|  Privacy policy     | Click      |  Displays privacy policy   |Pass

### Sign up Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|   Register button   | Click      |  Open Sign up form                                                |    Pass   |
|  User name  field   | Empty    |  Form won't submit error Displayed                                               |    Pass   |
|  User name  field   | Worng format entered    |  Form won't submit error Displayed                                               |    Pass   |
|  User name  field   | Duplicate Name   |  Form won't submit error Displayed                                               |    Pass   |
| Email  field (optional)  | Empty    |  Form submitted                                             |    Pass   |
| Email  field (optional)  | Worng format entered     |  Form won't submit error Displayed                                              |    Pass   |
| Email  field (optional)  |  Duplicate Email |  Form won't submit error Displayed                  |    Pass   |
| Email  field (optional)  | With correct format  |  Form submitted                                             |    Pass   |
| Password  field  | With incorrect format  |  Form won't submit error Displayed                                             |    Pass   |
| Password Confirmation field  | With incorrect Match  |  Form won't submit error Displayed                                             |    Pass   |
| Password  field  | With correct format  |  Form submitted                                             |    Pass   |
|  Sign Up button   | Click      |  Submit form and displays success login message                                              |    Pass   |
|  Contuine button on success message   | Click      |  redirects to home page message                                             |    Pass   |

### Home Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|  Order Now Button      | Click      |  Open Menu page                                                 |    Pass   |
### Menu Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|  Add to basket Button      | Click      |  Add item to basket                                                 |    Pass   |
|  Category Navbar      | Click      | Displays only items in that category                                               |    Pass   |
|  Sort by      | Click      | Displays  by options                                            |    Pass   |
|  Search Bar    | type in word      | Displays  all options containing that word                                           |    Pass   |
| Item image      | Click      | Displays Menu detail page                                            |    Pass   |

### Menu detail Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|  Add to basket Button      | Click      |  Add item to basket                                                 |    Pass   |
|  Keep Shopping      | Click      | Displays menu page                                         |    Pass   |
|  
Leave review     | Click      | Displays review form page                                         |    Pass   | 
|  back to menu     | Click      | Displays menu page   | pass |
| Edit Button      | Click      |  Menu Managment page                                                 |    Pass   |

### Basket Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Update Button      | Click      |  Add item to increase quantiy to basket                                                 |    Pass   | 
| + Button      | Click      |  Add item to increase quantiy to basket                                                 |    Pass   |
| - Button      | Click      |  Remove item to decrease quantiy in basket                                                 |    Pass   |
| Remove Button      | Click      |  Remove item to decrease quantiy in basket                                                 |    Pass   |
| Keep Shopping Button      | Click      |  Returns to Menu page                                               |    Pass   |
| Next Button      | Click      | Leads to Delivery option page page                                               |    Pass   |
| Item image      | Click      | Leads to Item detail page page                                               |    Pass   |

### Delivery Option  Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
| Collection Button      | Click      |  Opens Checkout Page                                             |    Pass   | 
| Delivery Button order under €10     | Click      |  error message                                            |    Pass   | 
| Delivery Button order over €10     | Click      |              Opens Checkout Page                                  |    Pass   | 

### Checkout  Page
| Feature               | Action     | Expected Result                                                    | Pass/Fail |
|-----------------------|------------|--------------------------------------------------------------------|-----------|
|  Name input  |   empty |  error warning                                              |    Pass   | 
|  Email input  |   empty |  error warning                                              |    Pass   | 
|  Email input  |   empty |  error warning                                              |    Pass   | 
|  Email input  |   email address | no error warning                                              |    Pass   |


### [CI Pythoon linter](https://pep8ci.herokuapp.com/) was use to test python code.

| The Chip Shop file                   |    Result    | 
|-----------------------------|------------|
| <details><summary>Settings.py</summary><img src="./documentation/validator-images/settings.py.png"></details>             | These errors are django set up code.   |
| <details><summary>urls.py</summary><img src="./documentation/validator-images/chip-shop-url.png"></details>             | No errors   |
|<details><summary>views.py</summary><img src="./documentation/validator-images/chip-shop-views.png"></details>             | No errors   |



| Review App                  |    Result    | 
|-----------------------------|------------|
|<details><summary>views.py</summary><img src="./documentation/validator-images/review-views.png"></details>             | No errors   |
| <details><summary>urls.py</summary><img src="./documentation/validator-images/review-urls.png"></details>             | No errors   |
| <details><summary>models.py</summary><img src="./documentation/validator-images/review-models.png"></details>             | No errors   |
|<details><summary>forms.py</summary><img src="./documentation/validator-images/review-form.png"></details>             | No errors   |




|  Menu App                  |    Result    | 
|-----------------------------|------------|
|<details><summary>views.py</summary><img src="./documentation/validator-images/profile-views.png"></details>             | No errors   |
| <details><summary>urls.py</summary><img src="./documentation/validator-images/profiles.png"></details>             | No errors   |
| <details><summary>models.py</summary><img src="./documentation/validator-images/profiles-models.png"></details>             | No errors   |
|<details><summary>views.py</summary><img src="./documentation/validator-images/profile-views.png"></details>             | No errors   |


| Profile App                  |    Result    | 
|-----------------------------|------------|
|<details><summary>views.py</summary><img src="./documentation/validator-images/profile-views.png"></details>             | No errors   |
| <details><summary>urls.py</summary><img src="./documentation/validator-images/profiles.png"></details>             | No errors   |
| <details><summary>models.py</summary><img src="./documentation/validator-images/profiles-models.png"></details>             | No errors   |
|<details><summary>forms.py</summary><img src="./documentation/validator-images/profiles-form.png"></details>             | No errors   |
|<details><summary>widgets.py</summary><img src="./documentation/validator-images/menu-widgets.png"></details>             | No errors   |
|<details><summary>app.py</summary><img src="./documentation/validator-images/profile-apps.py.png"></details>             | No errors   |


| Inquiry App                 |    Result    | 
|-----------------------------|------------|
|<details><summary>views.py</summary><img src="./documentation/validator-images/inquiry-views.png"></details>             | No errors   |
| <details><summary>urls.py</summary><img src="./documentation/validator-images/inquiry-urls.png"></details>             | No errors   |
| <details><summary>models.py</summary><img src="./documentation/validator-images/inquiry-models.png"></details>             | No errors   |
|<details><summary>forms.py</summary><img src="./documentation/validator-images/inquiry-form.png"></details>             | No errors   |
|<details><summary>admin.py</summary><img src="./documentation/validator-images/inquiry-admin.png"></details>             | No errors   |


| Checkout  App                 |    Result    | 
|-----------------------------|------------|
|<details><summary>views.py</summary><img src="./documentation/validator-images/checkout-views.png"></details>             | No errors   |
| <details><summary>urls.py</summary><img src="./documentation/validator-images/checkout-urls.png"></details>             | No errors   |
| <details><summary>models.py</summary><img src="./documentation/validator-images/checkout-models.png"></details>             | No errors   |
|<details><summary>forms.py</summary><img src="./documentation/validator-images/inquiry-form.png"></details>             | No errors   |
|<details><summary>admin.py</summary><img src="./documentation/validator-images/inquiry-admin.png"></details>             | No errors   |
|<details><summary>webhook.py</summary><img src="./documentation/validator-images/checkout-webhook.png"></details>             | No errors   |
|<details><summary>webhookhandler.py</summary><img src="./documentation/validator-images/checkout-webhook-handler.png"></details>             | No errors   |
|<details><summary>webhook.py</summary><img src="./documentation/validator-images/checkout-webhook.png"></details>             | No errors   |
|<details><summary>signals.py</summary><img src="./documentation/validator-images/checkout-signals.png"></details>             | No errors   |
|<details><summary>context.py</summary><img src="./documentation/validator-images/checkout-context.png"></details>             | No errors   |







### HTML Validatior
#### [W3C](https://validator.w3.org/) was used for validation of Html and CSS
| Page                 |    Result    | 
|-----------------------------|------------|
|<details><summary>Checkout Success</summary><img src="./documentation/validator-images/checkout-success.png"></details>             | Error from Djanjo   |
| <details><summary>Base.html</summary><img src="./documentation/validator-images/base.html.png"></details>             |  Error from Djanjo   |
| <details><summary>Mobile Top Header</summary><img src="./documentation/validator-images/mobile-top.png"></details>             |  Error from Djanjo   |
| <details><summary>Base.html</summary><img src="./documentation/validator-images/base.html.png"></details>             |  Error from Djanjo   |
| <details><summary>Mobile Top Header</summary><img src="./documentation/validator-images/mobile-top.png"></details>             |  Error from Djanjo   |
| <details><summary>Footer.html</summary><img src="./documentation/validator-images/footer.html.png"></details>             |  Error from Djanjo   |
| <details><summary>Toast warning</summary><img src="./documentation/validator-images/toast-warning.png"></details>             |  Error from Djanjo   |
| <details><summary>Toast Info</summary><img src="./documentation/validator-images/toast-info.png"></details>             |  Error from Djanjo   |
| <details><summary>Toast Errors</summary><img src="./documentation/validator-images/toast-errors.png"></details>             |  Error from Djanjo   |
| <details><summary>500 Error Html</summary><img src="./documentation/validator-images/500.html.png"></details>             |  Error from Djanjo   |
| <details><summary>500 Error Html</summary><img src="./documentation/validator-images/500.html.png"></details>             |  Error from Djanjo   |
| <details><summary>Add Review</summary><img src="./documentation/validator-images/add-review.png"></details>             |  Error from Djanjo   |
All Html page test all page have errors remaining due to django.

### CSS Validatior

| File                |    Result    | 
|-----------------------------|------------|
|<details><summary>Base Css</summary><img src="./documentation/validator-images/base.css.png"></details>             | No Errors  |
|<details><summary>Checkout Css</summary><img src="./documentation/validator-images/checkout.css.png"></details>             | No Errors  |
|<details><summary>Profile Css</summary><img src="./documentation/validator-images/profile.css.png"></details>             | No Errors  |
All Css file pass validatiors with no errors or warnings

### JS Validatior

| File                 |    Result    | 
|-----------------------------|------------|
|<details><summary>Countryfields js</summary><img src="./documentation/validator-images/js-countryfields.png"></details>             | No Errors  |
|<details><summary>Stripe Elements Js</summary><img src="./documentation/validator-images/stripe-elements.js.png"></details>             | No Errors  |
|<details><summary>Quantity inpuy Js</summary><img src="./documentation/validator-images/quanitity_input.png"></details>             | No Errors  |


