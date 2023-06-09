### Sales API (Mini System)

Hi! I'm Building Mini Sales API System using Fastapi Framework.

##### features

- for the user allow to login (just using if it's superuser), register features is building but comment that.
- for product allow to user to create product, get all produdct, get specific product, update and delete product.
- for sales can create sales for product, get all sales, or get sales for product,
  also get sales using specific date, or through a range of date

| METHOD   | ROUTE                             | FUNCTIONALITY                         |
| -------- | --------------------------------- | ------------------------------------- |
| _POST_   | `api/auth/register/`              | create account                        |
| _POST_   | `api/auth/login/`                 | login                                 |
| _GET_    | `api/product/`                    | list all product                      |
| _POST_   | `api/product/`                    | create new product                    |
| _GET_    | `api/product/{product_id}/`       | get specific product                  |
| _PUT_    | `api/product/{product_id}/`       | update specific product               |
| _DELETE_ | `api/product/{product_id}/`       | delete specific product               |
| _POST_   | `api/sales/product/{product_id}/` | create new sales for specific product |
| _GET_    | `api/sales/product/{product_id}/` | get all sales for specific product    |
| _GET_    | `api/sales/`                      | get all sales                         |
| _GET_    | `api/sales/date/{sale_date}`      | get all sales in specific date        |
| _GET_    | `api/sales/date-range/`           | get all sales in range of date        |



#####  How to use projects
-  create new floder called 'sales_api' and move to floder.
- then clone this project using this command
```git clone https://github.com/mohammedashrafdagga/sales_api.git .```
- after that we must create new virtual environment using this command
```python -m venv venv```
- then active it
-  In window using this command ```venv/scripts/activate```
- in Lunix or Mac using this command ```source/bin/activate```
- using this command to install all library in `requirements.txt` file ```pip install -r requirements.txt```
- after that we must create `.env` file tp put variable using in project
- create new database in postgressql called `sales_api`
- in this file include `SECERT_KEY ` and Variable Using in `app.settings` file to connect with postgresql database
```DB_USERNAME=***
DB_PASSWORD=***
DB_SERVER=****
DB_NAME=sales_api
SECRET_KEY=****```
to create secert key using this command ```openssl rand -hex 32``` 
##### now can run the project using this command
`uvicorn main:app --reload `
