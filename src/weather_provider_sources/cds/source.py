#!/usr/bin/env python

#  -------------------------------------------------------
#  SPDX-FileCopyrightText: 2019-2024 Alliander N.V.
#  SPDX-License-Identifier: MPL-2.0
#  -------------------------------------------------------

from weather_provider_libraries.base_models.wpl_source import WeatherProviderSource
from weather_provider_libraries.data_classes.source_related import WPSourceIdentity


class CDS(WeatherProviderSource):
    """CDS source class."""
    def __init__(self):
        """..."""
        super().__init__(
            identity=WPSourceIdentity(
                id="cds",
                name="Climate Data Store",
                description="The Climate Data Store (CDS) is a service by the European Centre for "
                            "Medium-Range Weather Forecasts (ECMWF)."
                            "Data from the CDS is freely available using the license at: "
                            "https://cds.climate.copernicus.eu/api/v2/terms/static/licence-to-use-copernicus-products.pdf "
                            "Data can be considered unaltered outside of filtering and formatting unless specified "
                            "otherwise.",
                information_url="https://www.knmi.nl/over-het-knmi/about"
            )
        )
        """Initializes the CDS source class."""
        """
        self.load_model(ERA5SingleLevelsModel())
        self.load_model(ERA5LandModel())
        self.load_model(ERA5HybridModel())
        """
