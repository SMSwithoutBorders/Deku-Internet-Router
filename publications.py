"""
This program is free software: you can redistribute it under the terms
of the GNU General Public License, v. 3.0. If a copy of the GNU General
Public License was not distributed with this file, see <https://www.gnu.org/licenses/>.
"""

import datetime
import logging
from db import create_publication_entry, fetch_publication


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def store_publication(country_code, platform_name, source, gateway_client, status, date_time=None):
    """
    Store a new publication entry with correct status.

    Args:
        country_code (str): Country code.
        platform_name (str): Platform name.
        source (str): Source of publication.
        gateway_client (str): Gateway client.
        status (str): "published" if successful, "failed" if not.
        date_time (datetime, optional): Timestamp. Defaults to now.
    """
    publication_data = {
        'country_code': country_code,
        'platform_name': platform_name,
        'source': source,
        'status': status,
        'gateway_client': gateway_client,
        'date_time': date_time or datetime.datetime.now()
    }

    publication = create_publication_entry(publication_data)

    if status == "published":
        logging.info("Successfully stored published message: %s", publication.__data__)
    else:
        logging.error("Failed to store message: %s", publication.__data__)

    return publication

def create_publication_entry(country_code, platform_name, source, status, gateway_client, date_time=None):
    """Create a new metric entry in the database."""
    publication_data = {
        "country_code": country_code,
        "platform_name": platform_name,
        "source": source,
        "status": status,
        "gateway_client": gateway_client,
        "date_time": date_time or datetime.datetime.now(),
    }
    
    return create_publication_entry(publication_data)

def get_publication(start_date, end_date, filters=None):
    """Retrieve Publications with optional filters."""
    return fetch_publication(start_date, end_date, filters)