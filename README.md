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
