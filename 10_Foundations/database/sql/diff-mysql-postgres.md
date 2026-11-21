### mysql supports by postgres does not

- grouped statments (rename): PostgreSQL requires separate ALTER TABLE statements for each column you want to rename, it does not support:
  ```sql
  -- not supported in postgres
  alter table model
  rename column createdat to created_at,
  rename column updatedat to updated_at;

  -- supported in postgres: multiple `add column` statements
  ```
- `after` clause: to define position of column in table
- word `user` without quotes: user is reserved keyword in postgres, you need use `"user"` instead of `user`
- `timestamp on update`: in postgres, you need to update updated_at column during update statement
