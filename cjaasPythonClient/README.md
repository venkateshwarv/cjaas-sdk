# swagger-client
Something amazing, something special - the Customer Journey as a Service (CJaaS) is a core data layer to enable Journeys across products built upon serverless multi-cloud architecture, to be available as a SaaS service for applications inside and outside of Cisco. [**Cisco Experimental - Not For Production Use**]

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 0.5.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://journeys.cisco.com](https://journeys.cisco.com)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | SAS Signature

try:
    # Delete All Events Collected within Namespace(i.e Org)
    api_response = api_instance.clear_tape(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->clear_tape: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | SAS Signature
person = 'person_example' # str | Unique Person ID to filter by

try:
    # Delete Events Collected on Specific Person
    api_response = api_instance.clear_tape_by_person(authorization, person)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->clear_tape_by_person: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.CloudEvent() # CloudEvent | 
authorization = 'authorization_example' # str | SAS Signature

try:
    # Data sink accepts events that describe what occurred - when - by whom on every interaction across touchpoints and applications
    api_instance.data_sink(body, authorization)
except ApiException as e:
    print("Exception when calling DefaultApi->data_sink: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
sig = 'sig_example' # str | SAS Signature within QueryString
data = 'data_example' # str | CloudEvent Serialized as Base64 UTF8 String

try:
    # Data sink accepts events that describe what occurred - when - by whom on every interaction across touchpoints and applications
    api_instance.data_sink_get(sig, data)
except ApiException as e:
    print("Exception when calling DefaultApi->data_sink_get: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | SAS Signature
id = 'id_example' # str | Unique Person ID to clear data

try:
    # Journeys are built around a concept of Identity. An identity shapes how Journey is connected together. Get Identity by Id
    api_response = api_instance.identities(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->identities: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | SAS Signature
id = 'id_example' # str | Unique Person ID to apply action/query upon
alias = 'alias_example' # str | Unique Person ID to apply action/query upon (optional)

try:
    # Tie multiple duplicate Identities together to a unique single individual nondestructively (i.e soft merge) without modifying the Tape
    api_response = api_instance.identities_alias(authorization, id, alias=alias)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->identities_alias: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | SAS Signature
id = 'id_example' # str | Unique Person ID to clear data

try:
    # Delete a Identity
    api_response = api_instance.identities_delete(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->identities_delete: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | SAS Signature
filter = 'filter_example' # str | oData Filter Expressions to Slice/Dice Search, ex: type eq 'Add To Cart' (optional)
top = 56 # int | Limit to return latest x events (optional)

try:
    # The Tape holds running stream of customer journey events that arrive onto Data Sink from all channels - across mediums
    api_response = api_instance.journeys(authorization, filter=filter, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->journeys: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | SAS Signature
person = 'person_example' # str | Unique Person ID to filter by
filter = 'filter_example' # str | oData Filter Expressions to Slice/Dice Search, ex: type eq 'Add To Cart' (optional)
top = 56 # int | Limit to return latest x events (optional)

try:
    # The Tape holds running stream of customer journey events that arrive onto Data Sink from all channels - across mediums
    api_response = api_instance.journeys_by_person(authorization, person, filter=filter, top=top)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->journeys_by_person: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | SAS Signature
operation = 'operation_example' # str | Key Operation Type: list or create or rotate
id = 'id_example' # str | Unique Key name as set

try:
    # Create or Rotate or Delete a Specific Key
    api_response = api_instance.keys(authorization, operation, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->keys: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | SAS Signature
id = 'id_example' # str | Unique Key name to delete

try:
    # CJaaS APIs are designed to be accessed with Shared Access Signature(SAS) to resources without transmitting any actual sensitive keys(hello! API Keys) or even exchanging a password for a proxy such as oAuth bearer
    api_response = api_instance.keys_delete(authorization, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->keys_delete: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | SAS Signature

try:
    # List All SAS Keys
    api_response = api_instance.keys_list(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->keys_list: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.OnlineOrchestration() # OnlineOrchestration | 
person = 'person_example' # str | Unique Person ID to filter by
authorization = 'authorization_example' # str | Optional SAS Signature within Header (optional)
sig = 'sig_example' # str | Optional SAS Signature within QueryString (optional)

try:
    # Trigger a Online Orchestration such as Webex Walkin or Display Offer Or Chat Bot to intercept and modify your Customer's Journey Midway
    api_response = api_instance.online_orchestration_trigger(body, person, authorization=authorization, sig=sig)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->online_orchestration_trigger: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.ProfileViewBuilderTemplate() # ProfileViewBuilderTemplate | 
authorization = 'authorization_example' # str | SAS Signature
person_id = 'person_id_example' # str | Identifies the person for whom the profile view is requested

try:
    # A Profile is a bespoke view of a customer's journey
    api_response = api_instance.profile_builder(body, authorization, person_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->profile_builder: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
sig = 'sig_example' # str | Optional SAS Signature within QueryString (optional)
authorization = 'authorization_example' # str | Optional SAS Signature within Header (optional)

try:
    # Real-time streaming enables API consumers to listen for events as it arrives part of the Journey, these may be transformed, value added / enriched and ready to be consumed or forwarded to an another destination
    api_response = api_instance.real_time_sse(sig=sig, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->real_time_sse: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
person = 'person_example' # str | Unique Person ID to filter by
sig = 'sig_example' # str | Optional SAS Signature within QueryString (optional)
authorization = 'authorization_example' # str | Optional SAS Signature within Header (optional)

try:
    # Real-time streaming enables API consumers to listen for events as it arrives part of the Journey, these may be transformed, value added / enriched and ready to be consumed or forwarded to an another destination
    api_response = api_instance.real_time_sse_person(person, sig=sig, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->real_time_sse_person: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str | SAS Signature

try:
    # API consumers can fully manage their Journey/CDP capabilities and settings using the Account Management endpoints
    api_response = api_instance.settings(authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->settings: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
body = swagger_client.AccountSettings() # AccountSettings | 
authorization = 'authorization_example' # str | SAS Signature

try:
    # API consumers can fully manage their Journey/CDP capabilities and settings using the Account Management endpoints
    api_response = api_instance.update_settings(body, authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->update_settings: %s\n" % e)

# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
person = 'person_example' # str | Unique Person ID to filter by
sig = 'sig_example' # str | Optional SAS Signature within QueryString (optional)
authorization = 'authorization_example' # str | Optional SAS Signature within Header (optional)

try:
    # SSE Channel for Webex Walkin Orchestration to Modify Journeys Midway
    api_response = api_instance.webex_walkin_sse(person, sig=sig, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->webex_walkin_sse: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://trycjaas.azurewebsites.net/*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**clear_tape**](docs/DefaultApi.md#clear_tape) | **DELETE** /ClearTape | Delete All Events Collected within Namespace(i.e Org)
*DefaultApi* | [**clear_tape_by_person**](docs/DefaultApi.md#clear_tape_by_person) | **DELETE** /ClearTape/{person} | Delete Events Collected on Specific Person
*DefaultApi* | [**data_sink**](docs/DefaultApi.md#data_sink) | **POST** /DataSink | Data sink accepts events that describe what occurred - when - by whom on every interaction across touchpoints and applications
*DefaultApi* | [**data_sink_get**](docs/DefaultApi.md#data_sink_get) | **GET** /DataSink | Data sink accepts events that describe what occurred - when - by whom on every interaction across touchpoints and applications
*DefaultApi* | [**identities**](docs/DefaultApi.md#identities) | **GET** /Identities | Journeys are built around a concept of Identity. An identity shapes how Journey is connected together. Get Identity by Id
*DefaultApi* | [**identities_alias**](docs/DefaultApi.md#identities_alias) | **GET** /Identities/alias | Tie multiple duplicate Identities together to a unique single individual nondestructively (i.e soft merge) without modifying the Tape
*DefaultApi* | [**identities_delete**](docs/DefaultApi.md#identities_delete) | **DELETE** /Identities | Delete a Identity
*DefaultApi* | [**journeys**](docs/DefaultApi.md#journeys) | **GET** /Journey | The Tape holds running stream of customer journey events that arrive onto Data Sink from all channels - across mediums
*DefaultApi* | [**journeys_by_person**](docs/DefaultApi.md#journeys_by_person) | **GET** /Journey/{person} | The Tape holds running stream of customer journey events that arrive onto Data Sink from all channels - across mediums
*DefaultApi* | [**keys**](docs/DefaultApi.md#keys) | **GET** /Keys/{operation}/{id} | Create or Rotate or Delete a Specific Key
*DefaultApi* | [**keys_delete**](docs/DefaultApi.md#keys_delete) | **DELETE** /Keys/{id} | CJaaS APIs are designed to be accessed with Shared Access Signature(SAS) to resources without transmitting any actual sensitive keys(hello! API Keys) or even exchanging a password for a proxy such as oAuth bearer
*DefaultApi* | [**keys_list**](docs/DefaultApi.md#keys_list) | **GET** /Keys/list | List All SAS Keys
*DefaultApi* | [**online_orchestration_trigger**](docs/DefaultApi.md#online_orchestration_trigger) | **POST** /Orchestration/Trigger/{person} | Trigger a Online Orchestration such as Webex Walkin or Display Offer Or Chat Bot to intercept and modify your Customer&#x27;s Journey Midway
*DefaultApi* | [**profile_builder**](docs/DefaultApi.md#profile_builder) | **POST** /Profileview | A Profile is a bespoke view of a customer&#x27;s journey
*DefaultApi* | [**real_time_sse**](docs/DefaultApi.md#real_time_sse) | **GET** /Real-time | Real-time streaming enables API consumers to listen for events as it arrives part of the Journey, these may be transformed, value added / enriched and ready to be consumed or forwarded to an another destination
*DefaultApi* | [**real_time_sse_person**](docs/DefaultApi.md#real_time_sse_person) | **GET** /Real-time/{person} | Real-time streaming enables API consumers to listen for events as it arrives part of the Journey, these may be transformed, value added / enriched and ready to be consumed or forwarded to an another destination
*DefaultApi* | [**settings**](docs/DefaultApi.md#settings) | **GET** /Settings | API consumers can fully manage their Journey/CDP capabilities and settings using the Account Management endpoints
*DefaultApi* | [**update_settings**](docs/DefaultApi.md#update_settings) | **POST** /Settings | API consumers can fully manage their Journey/CDP capabilities and settings using the Account Management endpoints
*DefaultApi* | [**webex_walkin_sse**](docs/DefaultApi.md#webex_walkin_sse) | **GET** /Walkin/{person} | SSE Channel for Webex Walkin Orchestration to Modify Journeys Midway

## Documentation For Models

 - [AccountSettings](docs/AccountSettings.md)
 - [CloudEvent](docs/CloudEvent.md)
 - [Object](docs/Object.md)
 - [OnlineOrchestration](docs/OnlineOrchestration.md)
 - [ProfileAttributeView](docs/ProfileAttributeView.md)
 - [ProfileViewBuilderTemplate](docs/ProfileViewBuilderTemplate.md)
 - [ProfileViewBuilderTemplateAttribute](docs/ProfileViewBuilderTemplateAttribute.md)
 - [ProfileViewQueryResponse](docs/ProfileViewQueryResponse.md)

## Documentation For Authorization


## authKey

- **Type**: API key
- **API key parameter name**: x-functions-key
- **Location**: HTTP header


## Author

cjaas-earlyaccess@cisco.com