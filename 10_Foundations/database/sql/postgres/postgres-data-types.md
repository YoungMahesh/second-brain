- Built-in Primitive Types:

  - INTEGER: Whole numbers
  - SERIAL: Auto-incrementing integer
  - BIGINT: Large integer
  - SMALLINT: Small integer
  - NUMERIC/DECIMAL: Precise decimal numbers
  - REAL/FLOAT: Floating-point numbers
  - TEXT: Variable-length string
  - VARCHAR: Variable-length character string
  - CHAR: Fixed-length character string
  - BOOLEAN: True/False values
  - DATE: Date values
  - TIMESTAMP: Date and time
  - INTERVAL: Time spans

- Enumerated Types (ENUM):

  - User-defined types with a fixed set of values
  - Restricts column to only allow predefined values
  - Example: `CREATE TYPE eye_color AS ENUM ('brown', 'blue', 'hazel', 'gray');`

- Array Types:

  - Can create arrays of any existing type
  - Example: `TEXT[], INTEGER[]`

- Composite Types:

  - Similar to structs in other languages
  - Can group multiple fields together

  ```sql
  CREATE TYPE address AS (
      street TEXT,
      city TEXT,
      zip_code VARCHAR(10)
  );
  ```

- Range Types:

  - Represent a range of values
  - Examples: int4range, tsrange

- JSON Types:

  - JSON: Strict JSON validation
  - JSONB: Binary JSON with indexing support

- Network Address Types:

  - INET: IP addresses
  - CIDR: Network addresses

- Geometric Types:

  - POINT: Geometric point
  - LINE: Geometric line
  - POLYGON: Geometric polygon

- Custom Domain Types:
  - User-defined types based on existing types with additional constraints
  ```sql
  CREATE DOMAIN positive_integer AS INTEGER
  CHECK (VALUE > 0);
  ```
