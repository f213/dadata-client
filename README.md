# dadata-client
Python client for dadata.ru APIs. Some parts of dadata.ru service are paid, so you may need to add your credentials from https://dadata.ru/profile/.

[![Build Status](https://travis-ci.org/f213/dadata-client.svg?branch=master)](https://travis-ci.org/f213/dadata-client)
[![codecov](https://codecov.io/gh/f213/dadata-client/branch/master/graph/badge.svg)](https://codecov.io/gh/f213/dadata-client)

## Installation

```bash
pip install dadata-client
```

## Usage

### Standartization client (paid)

```python
from dadata.standartization import DadataAddressStandartizationClient


dadata = DadataAddressStandartizationClient(
  key='<KEY>',
  secret='<SECRET>',
)

decomposed = dadata.request('Магадан, ул. Бывших строителей коммунизма, д. 5')

"""
  {
    "source": "мск сухонска 11/-89",
    "result": "г Москва, ул Сухонская, д 11, кв 89",
    "postal_code": "127642",
    "country": "Россия",
    "region_fias_id": "0c5b2444-70a0-4932-980c-b4dc0d3f02b5",
    "region_kladr_id": "7700000000000",
    "region_with_type": "г Москва",
    "region_type": "г",
    "region_type_full": "город",
    "region": "Москва",
    "area_fias_id": null,
    "area_kladr_id": null,
    "area_with_type": null,
    "area_type": null,
    "area_type_full": null,
    "area": null,
    "city_fias_id": null,
    "city_kladr_id": null,
    "city_with_type": null,
    "city_type": null,
    "city_type_full": null,
    "city": null,
    "city_area": "Северо-восточный",
    "city_district_fias_id": null,
    "city_district_kladr_id": null,
    "city_district_with_type": "р-н Северное Медведково",
    "city_district_type": "р-н",
    "city_district_type_full": "район",
    "city_district": "Северное Медведково",
    "settlement_fias_id": null,
    "settlement_kladr_id": null,
    "settlement_with_type": null,
    "settlement_type": null,
    "settlement_type_full": null,
    "settlement": null,
    "street_fias_id": "95dbf7fb-0dd4-4a04-8100-4f6c847564b5",
    "street_kladr_id": "77000000000283600",
    "street_with_type": "ул Сухонская",
    "street_type": "ул",
    "street_type_full": "улица",
    "street": "Сухонская",
    "house_fias_id": "5ee84ac0-eb9a-4b42-b814-2f5f7c27c255",
    "house_kladr_id": "7700000000028360004",
    "house_type": "д",
    "house_type_full": "дом",
    "house": "11",
    "block_type": null,
    "block_type_full": null,
    "block": null,
    "flat_type": "кв",
    "flat_type_full": "квартира",
    "flat": "89",
    "flat_area": "34.6",
    "square_meter_price": "198113",
    "flat_price": "6854710",
    "postal_box": null,
    "fias_id": "5ee84ac0-eb9a-4b42-b814-2f5f7c27c255",
    "fias_level": "8",
    "kladr_id": "7700000000028360004",
    "capital_marker": "0",
    "okato": "45280583000",
    "oktmo": "45362000",
    "tax_office": "7715",
    "tax_office_legal": "7715",
    "timezone": "UTC+3",
    "geo_lat": "55.8783675",
    "geo_lon": "37.6537388",
    "beltway_hit": "IN_MKAD",
    "beltway_distance": null,
    "qc_geo": 0,
    "qc_complete": 0,
    "qc_house": 2,
    "qc": 0,
    "unparsed_parts": null,
    "metro": [
      {
        "distance": 1.1,
        "line": "Калужско-Рижская",
        "name": "Бабушкинская"
      },
      {
        "distance": 1.2,
        "line": "Калужско-Рижская",
        "name": "Медведково"
      },
      {
        "distance": 2.5,
        "line": "Калужско-Рижская",
        "name": "Свиблово"
      }
    ]
  }
"""
```

### Find organisation client

``` python
from dadata.find_party import DadataFindPartyClient

dadata = DadataFindPartyClient(
  jey='<KEY>',
)

orgs = dadata.request('7707083893')

"""
[
  {
    "value": "ПАО СБЕРБАНК",
    "unrestricted_value": "ПАО СБЕРБАНК",
    "data": {
      "kpp": "773601001",
      "capital": {
        "type": "УСТАВНЫЙ КАПИТАЛ",
        "value": 67760844000
      },
      "management": {
        "name": "Греф Герман Оскарович",
        "post": "Президент, председатель правления"
      },
      "founders": [
        {
          "ogrn": null,
          "inn": "7702235133",
          "name": "ЦЕНТРАЛЬНЫЙ БАНК РОССИЙСКОЙ ФЕДЕРАЦИИ",
          "hid": "33b78a80c782d847d02a7e7a53d3aa17a5dff9a1cb5ec73d0311423dcc065a89",
          "type": "LEGAL",
          "share": null
        }
      ],
      "managers": [
        {
          "inn": "770303580308",
          "fio": {
            "surname": "Греф",
            "name": "Герман",
            "patronymic": "Оскарович",
            "gender": "MALE",
            "source": "ГРЕФ ГЕРМАН ОСКАРОВИЧ",
            "qc": null
          },
          "post": "Президент, председатель правления",
          "hid": "8aca73ef155e20b8ba6687d23521630e8fbe9b505b388cb9cb12eb1c43b68253",
          "type": "EMPLOYEE"
        }
      ],
      "branch_type": "MAIN",
      "branch_count": 93,
      "source": null,
      "qc": null,
      "hid": "145a83ab38c9ad95889a7b894ce57a97cf6f6d5f42932a71331ff18606edecc6",
      "type": "LEGAL",
      "state": {
        "status": "ACTIVE",
        "actuality_date": 1521590400000,
        "registration_date": 677376000000,
        "liquidation_date": null
      },
      "opf": {
        "type": "2014",
        "code": "12247",
        "full": "Публичное акционерное общество",
        "short": "ПАО"
      },
      "name": {
        "full_with_opf": "ПУБЛИЧНОЕ АКЦИОНЕРНОЕ ОБЩЕСТВО \"СБЕРБАНК РОССИИ\"",
        "short_with_opf": "ПАО СБЕРБАНК",
        "latin": null,
        "full": "СБЕРБАНК РОССИИ",
        "short": "СБЕРБАНК"
      },
      "inn": "7707083893",
      "ogrn": "1027700132195",
      "okpo": null,
      "okved": "64.19",
      "okveds": [
        {
          "main": true,
          "type": "2014",
          "code": "64.19",
          "name": "Денежное посредничество прочее"
        }
      ],
      "authorities": {
        "fts_registration": {
          "type": "FEDERAL_TAX_SERVICE",
          "code": "7700",
          "name": "Управление Федеральной налоговой службы по г.Москве",
          "address": "125284, г.Москва, Хорошевское ш., 12А"
        },
        "fts_report": {
          "type": "FEDERAL_TAX_SERVICE",
          "code": "7736",
          "name": "Инспекция Федеральной налоговой службы № 36 по г.Москве",
          "address": null
        },
        "pf": {
          "type": "PENSION_FUND",
          "code": "087705",
          "name": "Государственное учреждение - Главное Управление Пенсионного фонда РФ №4 Управление №1 по г. Москве и Московской области муниципальный район Гагаринский г.Москвы",
          "address": null
        },
        "sif": {
          "type": "SOCIAL_INSURANCE_FUND",
          "code": "7706",
          "name": "Филиал №6 Государственного учреждения - Московского регионального отделения Фонда социального страхования Российской Федерации",
          "address": null
        }
      },
      "documents": {
        "fts_registration": {
          "type": "FTS_REGISTRATION",
          "series": "77",
          "number": "4856976",
          "issue_date": 1029456000000,
          "issue_authority": "7700"
        },
        "pf_registration": {
          "type": "PF_REGISTRATION",
          "series": null,
          "number": "087705007215",
          "issue_date": 1283472000000,
          "issue_authority": "087705"
        },
        "sif_registration": {
          "type": "SIF_REGISTRATION",
          "series": null,
          "number": "770600307277061",
          "issue_date": 978566400000,
          "issue_authority": "7706"
        }
      },
      "licenses": [
        {
          "series": null,
          "number": "045-02894-100000",
          "issue_date": 975283200000,
          "issue_authority": "Центральный банк Российской Федерации",
          "suspend_date": null,
          "suspend_authority": null,
          "valid_from": 1444089600000,
          "valid_to": null,
          "activities": [
            "Брокерская деятельность"
          ],
          "addresses": [
            "Г. МОСКВА"
          ]
        }
      ],
      "address": {
        "value": "г Москва, ул Вавилова, д 19",
        "unrestricted_value": "г Москва, Академический р-н, ул Вавилова, д 19"
      },
      "phones": null,
      "emails": null,
      "ogrn_date": 1029456000000,
      "okved_type": "2014"
    }
  }
]
"""
```

## Credits

* [cryptomaniac512](http://github.com/cryptomaniac512)
