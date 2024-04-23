#!/usr/bin/env python

#  -------------------------------------------------------
#  SPDX-FileCopyrightText: 2019-2024 Alliander N.V.
#  SPDX-License-Identifier: MPL-2.0
#  -------------------------------------------------------

from weather_provider_libraries.base_models.wpl_source import WeatherProviderSource
from weather_provider_libraries.data_classes.source_related import WPSourceIdentity


class KNMI(WeatherProviderSource):
    """KNMI source class."""
    def __init__(self):
        """..."""
        super().__init__(
            identity=WPSourceIdentity(
                id="kmni",
                name="KMNI",
                description="The KNMI "
                            "(Royal Dutch Meteorological Institute) "
                            "is the Dutch national weather forecasting service."
                            "The KMNI takes part in the European Open Data initiative and as such most data is freely "
                            "available under either the [CC BY 4.0] license or the [CC0 1.0] license.",
                information_url="https://www.knmi.nl/over-het-knmi/about"
            )
        )
        """Initializes the KNMI source class."""
        """
        self.load_model(DagGegevensModel())
        self.load_model(UurGegevensModel())
        self.load_model(PluimModel())
        self.load_model(HarmonieAromeModel())
        self.load_model(WaarnemingenModel())
        self.load_model(WaarnemingenAggregateModel())
        self.load_model(WeerAlarmModel())
        """
