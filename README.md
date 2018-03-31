# bluecoat-sitereview
This code provides a way to query BlueCoat SiteReview for the current categorization of a URL, IP, or Domain name.  You can also submit a new review request with suggested category directly to BlueCoat.

## Install
The following modules must be installed in order to use bluecoat-sitereview.
* requests
* simplejson
* PIL
* pytesseract

With the prerequisite modules installed, run `python setup.py install` to complete the installation.

## Example Usage
```
>>> import bluecoat
>>> s = bluecoat.SiteReviewRequest('http://www.badsite.com')
>>> 
>>> s.CurrentRating()
u'Placeholders'
>>>
>>> s.SubmitRating('Suspicious','username@emailaddress.com')
>>>
```
