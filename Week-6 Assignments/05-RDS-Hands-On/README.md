# 05 - Setting Up and Using RDS

## Goal

Stand up a real database on Floci and interact with it directly using `psql` - no Python, just the same SQL you already know.

## Quick psql Primer (Read This First)

`psql` hasn't come up anywhere earlier in this program, so before diving in: it's just a command-line way of running the same SQL you already know how to write - it's not a new SQL dialect, just a new interface for typing it. A few things to know going in:

- Every SQL statement still ends in a semicolon (`;`), same as always. If you press Enter and nothing happens, you probably forgot it.
- `psql` also has its own "meta-commands," which are different from SQL and start with a backslash - you won't type SQL for these:
  - `\dt` - list the tables in the current database
  - `\d practice_orders` - describe a specific table's columns
  - `\q` - quit and return to your normal terminal
- Once connected, you'll see a prompt like `postgres=>` - that's psql waiting for either a SQL statement or one of the meta-commands above.

That's genuinely the whole learning curve. Everything else below is SQL you've already written before.

## Steps

1. **Create a DB instance:**
   ```
   aws --endpoint-url=http://localhost:4566 rds create-db-instance \
     --db-instance-identifier candidate-practice-db \
     --db-instance-class db.t3.micro \
     --engine postgres \
     --master-username postgres \
     --master-user-password postgres \
     --allocated-storage 5
   ```

2. **Describe it** to find the connection endpoint:
   ```
   aws --endpoint-url=http://localhost:4566 rds describe-db-instances \
     --db-instance-identifier candidate-practice-db \
     --query 'DBInstances[0].Endpoint'
   ```

3. **Connect with `psql`** using the host/port from the previous step:
   ```
   psql -h <endpoint-address> -p <port> -U postgres -d postgres
   ```
   (Password is `postgres`, matching what you set in Step 1.)

4. **Run the provided setup script** to create and populate a table - either paste its contents into your `psql` session, or run it directly from your regular terminal without opening a session first:
   ```
   psql -h <endpoint-address> -p <port> -U postgres -d postgres -f src/setup/setup.sql
   ```

5. **Confirm the table exists**, using a meta-command instead of SQL:
   ```
   \dt
   ```

6. **Query it back** to confirm the data is really there - this part is exactly the SELECT syntax you already know:
   ```sql
   SELECT * FROM practice_orders;
   ```

## On Your Own

Create a second table, `practice_customers` (with at least `id` and `name` columns), and add a `customer_id` foreign key column to `practice_orders` linking the two. Insert a couple of rows into `practice_customers`, update a few `practice_orders` rows to reference them, then write a `JOIN` query that returns each order alongside its customer's name.

## Submit

A screenshot of your `psql` session showing the setup script running, the `\dt` output, and the query from Step 6, plus a screenshot of your `JOIN` query and its output.
