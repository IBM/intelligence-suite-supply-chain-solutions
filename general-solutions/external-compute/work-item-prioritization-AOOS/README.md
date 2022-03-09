# Tutorial on Work Item Priority Score

## Work Item Priority Score

* The field `priority` (integer) is defined in work item business object.
* The primary use of this field is to estimate the severity of work items and can be used to sort the work items.
* Howevere, there are no in-built functions to calculate or estimate this value. Users can define their own business logic to calculate this value.
* This tutorial illustrates how a user can define a non-trivial business logic to estimate the prioirty score of a work item (_approaching out of stock_) and upsert the same to InfoHub.


## Python Notebooks

1. [InfoHub.ipynb](InfoHub.ipynb)
  * This notebook contains the basic transports connection to InfoHub and the required GraphQL queries.
  * First run this notebook in order to import the `InfoHubConnection` class.
2. [Upsert-AOOS-Priority-Score.ipynb](Upsert-AOOS-Priority-Score.ipynb)
  * The basic steps in upserting priority score are illustrated.
  * The function to calculate priority score `AOOS_priority_score` is predefined.
3. [AOOS-Priority-Score.ipynb](AOOS-Priority-Score.ipynb)
  * Accompanying optional notebook that explains the priority score business logic for _approaching out of stock_.
  * Users can experiment and analyze how the business logic works and is useful for estimating the config parameters.
  * The folders `data` and `figs` are associated with this notebook.
    * The input data are in folder `data`
    * Figures generated in the experimentation or analysis are stored in folder `figs`
  
### Basic Procedure

* Run `InfoHub.ipynb`, followed by `Upsert-AOOS-Priority-Score.ipynb`
