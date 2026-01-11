# dataframe_generator

# `df_gen` — Synthetic DataFrame Generator

The `df_gen` class is a flexible synthetic data generator designed to create realistic, customizable pandas DataFrames for analytics, modeling, testing, and instruction. Columns are added declaratively using `.add_column()` with a specified **column type**, **parameters**, and optional **metadata controls** such as missing values and rounding.

---

## Core Features

### Initialization

```python
df_gen(rows, random_state=None)
```

* `rows`: Number of rows to generate
* `random_state` *(default: None)*: Sets NumPy and Python random seeds for reproducibility
* Initializes an empty DataFrame and a schema metadata tracker

---

### Missing Values

All column types support missing values via a dictionary:

```python
{"missing": 0.10}
```

* Randomly replaces a percentage of values with `NaN`
* Default: `0.0` (no missing values)

---

### Rounding

Numeric columns support rounding:

```python
{"round": 2}
```

* Applied after generation and missingness
* Default: no rounding

---

### Metadata Tracking

Every added column is recorded with:

* Column name
* Column type
* Parameters
* Missing percentage
* Rounding

Access via:

```python
describe_schema()
```

---

## Column Types

---

## 1. Manual / Explicit Data

### `manual`

Inserts user-provided values.

**Parameters**

* `values`: Iterable of values
* `mixed` *(default: False)*: Shuffle values before repetition

```python
("manual", values, mixed)
```

---

## 2. Numeric Columns

### `int`

Random integers (inclusive).

**Parameters**

* `low`
* `high`

```python
("int", low, high)
```

---

### `int_list`

Samples from a fixed set of integers.

**Parameters**

* `values`
* `probs` *(default: None → uniform)*

```python
("int_list", values, probs)
```

---

### `uniform` / `double` / `decimals`

Uniform continuous distribution.

**Parameters**

* `low`
* `high`

```python
("uniform", low, high)
```

---

### `percent`

Beta-distributed proportions.

**Parameters**

* `alpha`
* `beta`
* `make_percent` *(default: False)*

```python
("percent", alpha, beta, make_percent)
```

---

## 3. Boolean Columns

### `bool`

Random True/False values.

```python
("bool",)
```

---

### `bernoulli`

Bernoulli trial.

**Parameter**

* `p`: Probability of True

```python
("bernoulli", p)
```

---

## 4. Categorical Columns

### `category` / `choice`

Uniform categorical sampling.

**Parameter**

* `categories`

```python
("category", categories)
```

---

### `category_prob` / `category_weighted`

Weighted categorical sampling.

**Parameters**

* `categories`
* `probs` *(must sum to 1)*

```python
("category_prob", categories, probs)
```

---

## 5. String Columns

### `string`

Random character strings.

**Parameters**

* `length`
* `case` *(default: "both")*

```python
("string", length, case)
```

---

## 6. Identifier Columns

### `id`

Sequential numeric ID.

**Parameter**

* `start` *(default: 1)*

```python
("id", start)
```

---

### `prefix_id`

Prefixed numeric identifier.

**Parameters**

* `prefix`
* `width`
* `unique` *(default: False)*

```python
("prefix_id", prefix, width, unique)
```

---

### `alphanumeric_id`

Random alphanumeric identifier.

**Parameters**

* `length`
* `unique` *(default: True)*

```python
("alphanumeric_id", length, unique)
```

---

## 7. Name & Contact Columns

### `names`

Generates realistic first and last names.

**Parameter**

* `unique` *(default: True)*

Creates two columns:

* `first_name`
* `last_name`

```python
("names", unique)
```

---

### `email`

Generates email addresses.

**Parameter**

* `domains` *(default: ["gmail.com", "yahoo.com", "outlook.com"])*

Uses existing `first_name` and `last_name` columns if available.

```python
("email", domains)
```

---

### `phone`

Generates U.S.-style phone numbers.

**Parameters**

* `area_codes` *(default: preset list)*
* `format` *(default: "US")*

```python
("phone", area_codes, format)
```

---

## 8. Geographic Columns

### `state`

U.S. states.

**Parameter**

* `abrv` *(default: False → full names)*

```python
("state", abrv)
```

---

### `country`

Country generator.

**Parameters**

* `mode` *(default: "name")*
* `weighted` *(default: False)*

```python
("country", mode, weighted)
```

---

## 9. Date & Time Columns

### `date`

Random calendar dates.

**Parameters**

* `start_date`
* `end_date`

```python
("date", start_date, end_date)
```

---

### `datetime`

Random timestamps.

**Parameters**

* `start_date`
* `end_date`

```python
("datetime", start_date, end_date)
```

---

### `dob_from_age`

Computes date of birth from an age column.

**Parameter**

* `age_column`

Adds randomized birthday jitter.

```python
("dob_from_age", age_column)
```

---

### `age_from_dob`

Computes age from date of birth.

**Parameter**

* `dob_column`

Correctly accounts for birthdays.

```python
("age_from_dob", dob_column)
```

---

## 10. Statistical Distributions

### `normal`

Normal (Gaussian) distribution.

**Parameters**

* `mean`
* `sd`

```python
("normal", mean, sd)
```

---

### `normal_clip`

Bounded normal distribution.

**Parameters**

* `mean`
* `sd`
* `min`
* `max`

```python
("normal_clip", mean, sd, min, max)
```

---

### `lognormal`

Log-normal distribution.

**Parameters**

* `mean` *(mean of log values)*
* `sigma` *(standard deviation of log values)*

```python
("lognormal", mean, sigma)
```

---

### `poisson`

Poisson-distributed counts.

**Parameter**

* `lam`

```python
("poisson", lam)
```

---

### `beta`

Scaled beta distribution.

**Parameters**

* `alpha`
* `beta`
* `max_value`

```python
("beta", alpha, beta, max_value)
```

---

### `exponential`

Exponential distribution.

**Parameter**

* `scale`

```python
("exponential", scale)
```

---

### `gamma`

Gamma distribution.

**Parameters**

* `shape`
* `scale`

```python
("gamma", shape, scale)
```

---

## 11. Time Series & Trends

### `trend`

Linear trend with noise.

**Parameters**

* `start`
* `slope`
* `noise_sd`

```python
("trend", start, slope, noise_sd)
```

---

## 12. Inter-Column Dependencies

### `correlated`

Linear correlation with an existing column.

**Parameters**

* `base_column`
* `slope`
* `noise_sd`

```python
("correlated", base_column, slope, noise_sd)
```

---

### `conditional`

Conditional value assignment.

**Parameters**

* `condition_column`
* `condition_value`
* `true_value`
* `false_value`

```python
("conditional", condition_column, value, true_value, false_value)
```

---

### `computed`

Custom column computed from existing columns.

**Parameters**

* `function`
* `dependent_columns`

```python
("computed", func, columns)
```

---

## 13. Analytics & Feature Engineering

### Rolling Metrics

All rolling metrics share the same structure.

**Defaults**

* `min_periods = window`

Available types:

* `rolling_mean`
* `rolling_sum`
* `rolling_std`
* `rolling_max`
* `rolling_min`

```python
("rolling_mean", base_column, window, min_periods)
```

---

### `zscore`

Standardized z-score.

**Parameter**

* `base_column`

```python
("zscore", base_column)
```

---

### `bin`

Discretizes numeric values.

**Parameters**

* `base_column`
* `bins`
* `labels`

```python
("bin", base_column, bins, labels)
```

---

### `pct_change`

Percent change between rows.

**Parameter**

* `base_column`

```python
("pct_change", base_column)
```

---

## 14. Duplicates

### `add_duplicates()`

Introduces controlled duplication into an existing column.

**Parameters**

* `column_name`
* `duplicate_rate` *(default: 0.10)*

---

## Output

### `build()`

Returns a copy of the generated DataFrame.

---

### `to_csv(path)`

Exports the DataFrame to CSV.

