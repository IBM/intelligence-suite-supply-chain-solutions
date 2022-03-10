# Work Item Prioritization

## Work Item Priority Score

* The field `priority` (integer) is defined in work item business object.
* The primary use of this field is to estimate the severity of work items and can be used to sort the work items within a work queue.
* Howevere, there are no in-built functions to calculate or estimate this value. Users can define their own business logic to calculate this value via external compute.
* This tutorial illustrates how a user can define a non-trivial business logic to estimate the prioirty score of a work item in _approaching out of stock_ (AOOS) work queue, and upsert the same to SCIS/InfoHub.


## Python Notebooks

1. [InfoHub.ipynb](InfoHub.ipynb)
  * This notebook contains the basic transports connection to InfoHub and the required GraphQL queries.
  * First run this notebook in order to import the `InfoHubConnection` class.
2. [Upsert-AOOS-Priority-Score.ipynb](Upsert-AOOS-Priority-Score.ipynb)
  * The basic steps in upserting priority score are illustrated.
  * The function to calculate priority score `AOOS_priority_score` is predefined.
  * Useful for quick implementation and adoption.
3. [Upsert-AOOS-Priority-Score-Demo.ipynb](Upsert-AOOS-Priority-Score-Demo.ipynb)
  * Detailed demo of illustrating change in priority score of a AOOS work item with changes in supply/demand plans.
  * Extension of [Upsert-AOOS-Priority-Score.ipynb](Upsert-AOOS-Priority-Score.ipynb) with inclusion of events simulating change in supply/demand plans.
4. [AOOS-Priority-Score.ipynb](AOOS-Priority-Score.ipynb)
  * Accompanying optional notebook that explains the priority score business logic for _approaching out of stock_.
  * Users can experiment and analyze how the business logic works and is useful for estimating the config parameters.
  * Useful for extending the business logic and for implementing new business logic for other work queues.
  * Uses pre-defined data in CSV and does not require live connection to SCIS/InfoHub
  * The folders `data` and `figs` are associated with this notebook.
    * The input data are in folder `data`
    * Figures generated in the experimentation or analysis are stored in folder `figs`
  
### Possible Runs

* **Demo**: Run `InfoHub.ipynb`, followed by interactive `Upsert-AOOS-Priority-Score-Demo.ipynb` (requires active SCIS account)
* **Basic**: Run `InfoHub.ipynb`, followed by interactive `Upsert-AOOS-Priority-Score.ipynb` (requires active SCIS account)
* **Experimentation**: `AOOS-Priority-Score.ipynb` - interactive notebook for understanding the business logic

### Prerequisites

* Active SCIS account required for **Demo** and **Basic** runs
  * Add your credentials to `credentials.json-example` and rename it to `credentials.json`
  * (Repo Collaborators): `credentials.json` is included in `.gitignore` and hence will not expose your credentials accidentally in your git commits.
* Configure AOOS work queue to show the `priority` field in the SCIS UI.
  * The notebooks will work without above configuration, but it is required to view the results in the UI.
* Assign the work items to yourself/someone (or move them to pending).
  * Only when assigned, work item objects are created, and one can calculate the priority score.

### Contact

* Kamesh `kameshwaran.s@in.ibm.com`
* Pankaj `pankajdayama@in.ibm.com`
