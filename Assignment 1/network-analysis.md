# Network Analysis

## Website

**Google Search**

The Network activity was observed while loading the Google website in Google Chrome.

## Browser and Configuration

- **Browser:** Google Chrome
- **Panel:** DevTools → Network
- **Disable cache:** Enabled
- **Throttling:** No throttling
- **Page:** Google Search

## Network Results

### 1. Request Count

**110 requests**

The browser made 110 network requests while loading the page.

### 2. Total Page Size

The Network panel reports:

- **Transferred:** 2.4 MB
- **Resources:** 6.3 MB

The transferred size represents the data actually transferred over the network, while the resources value represents the total size of the loaded resources.

### 3. Single Slowest Resource

From the visible Network waterfall, the slowest resource shown in the request list is:

**`www.google.com`**

- **Type:** Prefetch
- **Status:** 200
- **Time:** 7.24 s

Therefore, the slowest visible request in the captured Network panel was `www.google.com`, taking approximately **7.24 seconds**.

### 4. 3xx/4xx Responses

The Network panel shows several requests with status:

**`204`**

Examples visible in the capture include:

- `client_204?...` — Status `204`
- `gen_204?...` — Status `204`
- `gen_204?...` — Status `204`
- `gen_204?...` — Status `204`

There were **no 3xx or 4xx status codes visible** in the captured request list.

A `204 No Content` response is a successful HTTP response indicating that the server processed the request but returned no response body.

## Waterfall Observations

The Network waterfall shows that Google loads many resources in parallel. These include scripts, stylesheets, images, documents, and background/ping requests.

Some visible examples are:

| Resource Type | Example Status | Approx. Time |
|---|---:|---:|
| WebP image | 200 | 1.88 s |
| Script | 200 | 1.93 s |
| Document | 200 | 2.25 s |
| Script | 200 | 3.14–3.19 s |
| Ping | 204 | 3.83–5.90 s |
| Stylesheet | 200 | 5.82 s |
| Script | 200 | 5.85 s |
| Prefetch | 200 | 7.24 s |

The page reported:

- **110 requests**
- **2.4 MB transferred**
- **6.3 MB resources**
- **DOMContentLoaded:** 872 ms
- **Load:** 6.78 s
- **Finish:** 59.34 s

The difference between the page load time and the final finish time indicates that some background or additional network activity continued after the main page had loaded.

## Conclusion

With the browser cache disabled, the Google page generated **110 network requests** and transferred **2.4 MB** of data, with **6.3 MB** of resources loaded. The slowest visible request was the `www.google.com` prefetch request at approximately **7.24 seconds**. Several `204 No Content` responses were observed, but no 3xx or 4xx responses were visible in the captured Network panel.
