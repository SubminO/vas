import buildUrl from 'build-url';
import { API_URL, API_HEADERS } from '../constants';

function _buildUrl(path, query =null) {
  let params = {path: path};

  if (query) {
    params['queryParams'] = query;
  }

  return buildUrl(`${API_URL}`, params);
}


export default {
  retrieve: async (path, query =null) => {
    let url = _buildUrl(path, query);

    const response = await fetch(url, {
      method: 'GET',
      headers: API_HEADERS,
    });

    const _data = await response.json();

    if (response.status !== 200) {
      throw {
        status: response.status,
        text: response.statusText,
        data: _data,
      }
    }

    return _data;
  },
  create: async (path, query =null, data =null) => {
    let url = _buildUrl(path, query);

    if (!data) {
      data = {};
    }

    const response = await fetch(url, {
      method: 'POST',
      headers: API_HEADERS,
      body: JSON.stringify(data)
    });

    const _data = await response.json();
    if (response.status !== 201) {
      throw {
        status: response.status,
        text: response.statusText,
        data: _data,
      }
    }

    return _data;
  },
  update: async (path, query =null, data =null) => {
    let url = _buildUrl(path, query);

    if (!data) {
      data = {};
    }

    const response = await fetch(url, {
      method: 'PUT',
      headers: API_HEADERS,
      body: JSON.stringify(data)
    });

    const _data = await response.json();
    if (response.status !== 200) {
      throw {
        status: response.status,
        text: response.statusText,
        data: _data,
      }
    }

    return _data;
  },
  delete: async (path, query =null) => {
    let url = _buildUrl(path, query);

    const response = await fetch(url, {
      method: 'DELETE',
      headers: API_HEADERS,
    });

    if (response.status !== 204) {
      throw {
        status: response.status,
        text: response.statusText,
      }
    }
  }
}