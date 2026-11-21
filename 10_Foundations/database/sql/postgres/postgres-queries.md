```sql
-- postgres have case insensitive sql query syntax (including column-names)

create type eye_color as enum ('brown', 'blue', 'hazel', 'gray');
create table model (
    -- serial = auto-incrementing intenger column
    id serial primary key,
    person_id integer not null references person(id),
    -- in postgres, text is recommended for storing string most use cases where you don't need a strict length limit
    description text,
    name varchar(255) not null,
    age integer not null,
    eye_color eye_color NOT NULL default 'brown',
    bald boolean not null,
    createdAt timestamp not null default now(),
    updatedAt timestamp not null default now()

    pack_id integer not null,
    foreign key (pack_id) references pack(id) on delete cascade
);

alter table model
rename column updatedat to updated_at;
```
