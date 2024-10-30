
# FastAPI Documentation

**Version:** 0.1.0  
**OpenAPI Version:** OAS 3.1  
---

## GET /
**Summary:** Root

### Parameters  
_None_

### Responses  
| Code | Description            | Media Type        | Example Value |  
|------|------------------------|-------------------|---------------|  
| 200  | Successful Response    | `application/json` | `"string"`     |

---

## GET /posts
**Summary:** Get Posts

### Parameters  
_None_

### Responses  
| Code | Description            | Media Type        | Example Value |  
|------|------------------------|-------------------|---------------|  
| 200  | Successful Response    | `application/json` | `"string"`     |

---

## POST /posts
**Summary:** Create Posts

### Parameters  
_None_

### Request Body  
**Media Type:** `application/json`  
**Example Value:**
```json
{
  "title": "string",
  "content": "string",
  "published": true,
  "rating": 0
}
```

### Responses  
| Code | Description            | Media Type        | Example Value |  
|------|------------------------|-------------------|---------------|  
| 201  | Successful Response    | `application/json` | `"string"`     |  
| 422  | Validation Error       | `application/json` |  
```json
{
  "detail": [
    {
      "loc": ["string", 0],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

---

## GET /posts/{id}
**Summary:** Get Post

### Parameters  
- **id** (integer, path) – *Required*

### Responses  
| Code | Description            | Media Type        | Example Value |  
|------|------------------------|-------------------|---------------|  
| 200  | Successful Response    | `application/json` | `"string"`     |  
| 422  | Validation Error       | `application/json` |  
```json
{
  "detail": [
    {
      "loc": ["string", 0],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

---

## DELETE /posts/{id}
**Summary:** Delete Post

### Parameters  
- **id** (integer, path) – *Required*  
- **status_code** (integer, query) – *Default: 204*

### Responses  
| Code | Description            | Media Type        | Example Value |  
|------|------------------------|-------------------|---------------|  
| 204  | No Content (Successful)| -                 | -             |  
| 422  | Validation Error       | `application/json` |  
```json
{
  "detail": [
    {
      "loc": ["string", 0],
      "msg": "string",
      "type": "string"
    }
  ]
}
```

---

## PUT /posts/{id}
**Summary:** Update Post

### Parameters  
- **id** (integer, path) – *Required*

### Request Body  
**Media Type:** `application/json`

---

## Schemas
- **HTTPValidationError**: Represents validation errors with relevant details.
- **Post**: Describes the structure of a post (e.g., title, content, published, rating).
- **ValidationError**: Contains information about errors, including location, message, and type.
```

This version reflects the structure and key elements of the first 2 days of learning API development with Python.