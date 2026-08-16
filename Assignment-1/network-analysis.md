# Network Analysis

## Website Tested

**Website:** Yahoo Search (India)  
**URL:** `https://in.search.yahoo.com/search?fr=mcafee&type=E210IN826G0&p=google`

I opened the website in Google Chrome, opened **DevTools → Network**, enabled **Disable cache**, and reloaded the page. I then inspected the Network waterfall and sorted the requests by the **Time** column.

## Network Summary

| Metric | Observation |
|---|---:|
| Total requests | **41 requests** |
| Data transferred | **1.1 MB** |
| Total resources | **2.0 MB** |
| Finish time | **15.55 s** |
| DOMContentLoaded | **1.68 s** |
| Load event | **10.45 s** |
| Cache | **Disabled** |

## Single Slowest Resource

The slowest resource visible after sorting the Network panel by the **Time** column was:

- **Resource:** `voice-close-202105050733.wav`
- **Status:** `206`
- **Type:** Media
- **Size:** `150 kB`
- **Time:** **8.09 s**

A `206 Partial Content` response means the server returned only part of a resource, usually because the browser requested a byte range. This is normal for media files and is not an error.

The next slow resources visible were `yahoo-search-logo-51x14-2x.png` and `t_140x140`, both taking about **8.08 s**.

## 3xx / 4xx Responses

No **3xx (redirection)** or **4xx (client error)** responses were visible in the captured Network request list.

The visible responses were mainly `200 OK`, along with several `206 Partial Content` responses for media and a `204` response.

- **200 OK:** The request completed successfully.
- **204 No Content:** The request succeeded, but the server returned no response body.
- **206 Partial Content:** The server successfully returned only the requested portion of a resource.

## Observations

1. The page generated **41 network requests** during the reload.
2. The browser transferred approximately **1.1 MB** of data, while the total resources amounted to approximately **2.0 MB**.
3. The slowest visible request was the `voice-close-202105050733.wav` media resource at **8.09 seconds**.
4. Several JavaScript resources also took more than 7 seconds.
5. No 3xx or 4xx errors were observed in the captured request list.
6. Cache was disabled before reloading, as required by the assignment.

## Evidence

The accompanying screenshot shows the Chrome DevTools Network panel with **Disable cache enabled**, the request count, transferred data, resource size, and the sorted request times.
