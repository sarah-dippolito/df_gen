#imports
import numpy as np
import pandas as pd 
import string
import random

'''
Class that generates dataframes based on chosen column types and parameter values 
'''

# ai generated names
f_n = [
"James","Mary","John","Patricia","Robert","Jennifer","Michael","Linda","William","Elizabeth",
"David","Barbara","Richard","Susan","Joseph","Jessica","Thomas","Sarah","Charles","Karen",
"Christopher","Nancy","Daniel","Lisa","Matthew","Margaret","Anthony","Betty","Mark","Sandra",
"Donald","Ashley","Steven","Dorothy","Paul","Kimberly","Andrew","Emily","Joshua","Donna",
"Kenneth","Michelle","Kevin","Carol","Brian","Amanda","George","Melissa","Edward","Deborah",
"Ronald","Stephanie","Timothy","Rebecca","Jason","Laura","Jeffrey","Sharon","Ryan","Cynthia",
"Jacob","Kathleen","Gary","Amy","Nicholas","Angela","Eric","Shirley","Jonathan","Anna",
"Stephen","Brenda","Larry","Pamela","Justin","Emma","Scott","Nicole","Brandon","Helen",
"Benjamin","Samantha","Samuel","Katherine","Gregory","Christine","Alexander","Debra","Patrick","Rachel",
"Frank","Carolyn","Raymond","Janet","Jack","Catherine","Dennis","Maria","Jerry","Heather",
"Tyler","Diane","Aaron","Ruth","Jose","Julie","Henry","Olivia","Adam","Joyce",
"Douglas","Victoria","Nathan","Kelly","Peter","Christina","Zachary","Lauren","Kyle","Joan",
"Walter","Evelyn","Harold","Judith","Jeremy","Megan","Ethan","Cheryl","Carl","Andrea",
"Keith","Hannah","Roger","Martha","Gerald","Jacqueline","Christian","Frances","Terry","Gloria",
"Sean","Ann","Austin","Teresa","Arthur","Kathryn","Noah","Sara","Lawrence","Janice",
"Jesse","Jean","Joe","Alice","Bryan","Madison","Billy","Doris","Jordan","Abigail",
"Albert","Julia","Dylan","Judy","Bruce","Grace","Willie","Denise","Gabriel","Amber",
"Alan","Marilyn","Juan","Beverly","Logan","Danielle","Wayne","Theresa","Ralph","Sophia",
"Roy","Marie","Eugene","Diana","Randy","Brittany","Vincent","Natalie","Russell","Isabella",
"Louis","Charlotte","Philip","Rose","Bobby","Alexis","Johnny","Kayla","Bradley","Hailey",
"Leonard","Lillian","Martin","Faith","Caleb","Alyssa","Curtis","Savannah","Miguel","Audrey",
"Harvey","Brooklyn","Xavier","Claire","Kai","Paisley","Miles","Skylar","Jaxon","Lucy",
"Leo","Hudson","Nora","Eli","Scarlett","Asher","Zoey","Landon","Penelope",
"Maverick","Aria","Easton","Violet","Silas","Aurora","Declan","Hazel","Rowan","Willow",
"Finn","Ivy","Theo","Stella","Emmett","Elena","Jasper","Naomi","Atlas","Eva",
"Beckett","Luna","Sawyer","Camila","Micah","Gianna","Reid","Isla","Cole","Ruby",
"Max","Mila","Evan","Madeline","Luke","Piper","Owen","Clara","Isaac","Freya",
"Aiden","Adeline","Grayson","Quinn","Lincoln","Hadley","Wyatt","Sloane","Carter","Phoebe",
"Julian","Tessa","Ezra","June","Levi","Margot","Roman","Esme","Sebastian","Daphne",
"Dominic","Eliza","Bianca","Victor","Monica","Marcus","Vanessa","Jared","Paige",
"Jereimiah", "Eve"
]
l_n = [
"Smith","Johnson","Williams","Brown","Jones","Garcia","Miller","Davis","Rodriguez","Martinez",
"Hernandez","Lopez","Gonzalez","Wilson","Anderson","Thomas","Taylor","Moore","Jackson","Martin",
"Lee","Perez","Thompson","White","Harris","Sanchez","Clark","Ramirez","Lewis","Robinson",
"Walker","Young","Allen","King","Wright","Scott","Torres","Nguyen","Hill","Flores",
"Green","Adams","Nelson","Baker","Hall","Rivera","Campbell","Mitchell","Carter","Roberts",
"Gomez","Phillips","Evans","Turner","Diaz","Parker","Cruz","Edwards","Collins","Reyes",
"Stewart","Morris","Morales","Murphy","Cook","Rogers","Gutierrez","Ortiz","Morgan","Cooper",
"Peterson","Bailey","Reed","Kelly","Howard","Ramos","Kim","Cox","Ward","Richardson",
"Watson","Brooks","Chavez","Wood","James","Bennett","Gray","Mendoza","Ruiz","Hughes",
"Price","Alvarez","Castillo","Sanders","Patel","Myers","Long","Ross","Foster","Jimenez",
"Powell","Jenkins","Perry","Russell","Sullivan","Bell","Coleman","Butler","Henderson","Barnes",
"Gonzales","Fisher","Vasquez","Simmons","Romero","Jordan","Patterson","Alexander","Hamilton","Graham",
"Reynolds","Griffin","Wallace","Moreno","West","Cole","Hayes","Bryant","Herrera","Gibson",
"Ellis","Tran","Medina","Aguilar","Stevens","Murray","Ford","Castro","Marshall","Owens",
"Harrison","Fernandez","McDonald","Woods","Washington","Kennedy","Wells","Vargas","Henry","Chen",
"Freeman","Webb","Tucker","Guzman","Burns","Crawford","Olson","Simpson","Porter","Hunter",
"Gordon","Mendez","Silva","Shaw","Snyder","Mason","Dixon","Munoz","Hunt","Hicks",
"Holmes","Palmer","Wagner","Black","Robertson","Boyd","Rose","Stone","Salazar","Fox",
"Warren","Mills","Meyer","Rice","Schmidt","Garrett","Daniels","Ferguson","Nichols","Stephens",
"Soto","Weaver","Ryan","Gardner","Payne","Grant","Dunn","Kelley","Spencer","Hawkins",
"Arnold","Pierce","Vazquez","Hansen","Peters","Santos","Hart","Bradley","Knight","Elliott",
"Cunningham","Duncan","Armstrong","Hudson","Carroll","Lane","Riley","Andrews","Alvarado","Ray",
"Delgado","Berry","Perkins","Hoffman","Johnston","Matthews","Pena","Richards","Contreras","Willis",
"Carpenter","Lawrence","Sandoval","Guerrero","George","Chapman","Rios","Estrada","Ortega","Watkins",
"Greene","Nunez","Wheeler","Valdez","Harper","Burke","Larson","Santiago","Maldonado","Morrison",
"Franklin","Carlson","Austin","Dominguez","Carr","Lawson","Jacobs","Obrien","Lynch","Singh",
"Vega","Bishop","Montgomery","Oliver","Jensen","Harvey","Williamson","Gilbert","Dean","Sims",
"Espinoza","Howell","Li","Wong","Fowler","Reid","Hanson","Le","McCarthy","Khan",
"Schultz","Walters","Barrett","Bowman","Mcdaniel","McGuire","Zhang","Ali","Patton","Hubbard",
"Glass","Hooper","Lloyd","Mejia","Kramer","Montoya","Baldwin","Avila","Serrano","Hogan"
]

# class to generate dataframes
class df_gen:
    
    def __init__(self, rows, random_state=None):
        self.rows = rows
        self.random_state = random_state
        if random_state is not None:
            np.random.seed(random_state)
            random.seed(random_state)
        self.df = pd.DataFrame(index=range(rows))
        self.metadata = []
    
    # function to add a certain percentage of missing values to a column 
    def missing_add(self, col, m_percent):
        if m_percent<=0:
            return col
        num_missing = round(self.rows * m_percent)
        mask = random.sample(range(self.rows), num_missing)
        col = col.copy()
        col[mask] = np.nan
        return col
    
    # function to round numerical columns
    def round_data(self, col, num_round):
        return round(col, num_round)
    
    # introduce duplicates into an existing column
    def add_duplicates(self, column_name, duplicate_rate=0.1):
        col = self.df[column_name].copy()
        n_duplicates = int(len(col) * duplicate_rate)
        dup_indices = np.random.choice(len(col), n_duplicates, replace=True)
        source_indices = np.random.choice(len(col), n_duplicates)
        col.iloc[dup_indices] = col.iloc[source_indices].values
        self.df[column_name] = col
        return self

    
    # show metadata
    def describe_schema(self):
        return pd.DataFrame(self.metadata)

    # export data as csv file
    def to_csv(self, path):
        self.df.to_csv(path, index=False)

    
    # function to add columns
    def add_column(self, name, part):
        col_type = part[0]
        extras = part[-1] if isinstance(part[-1], dict) else {}
        m_percent = extras.get("missing", 0.0)
        round_num = extras.get("round", None)

        
        ### column options
        
        ### manuala
        
        # manual (parameters: data to insert, if mixed)
        if col_type == "manual":
            values = list(part[1])
            mixed = part[2] if len(part) > 2 else False
            if len(values) == 0:
                raise ValueError("Manual column values cannot be empty.")
            data = []
            while len(data) < self.rows:
                temp = values.copy()
                if mixed:
                    random.shuffle(temp)
                data.extend(temp)

            data = data[:self.rows]

            
        
        ### numerical 
        
        # integer column (parameters: low, high)
        elif col_type == "int":
            low, high = part[1], part[2]
            data = np.random.randint(low, high+1, self.rows)
        
        # column with set integers and probability of each being selected (parameters: values, probabilities [if probabilities is None all integers have equal chance of being selected])
        elif col_type == "int_list":
            values, probs = part[1], part[2]
            if probs is not None and not np.isclose(sum(probs), 1):
                raise ValueError("Probabilities must sum to 1.")
            if probs == None:
                data = np.random.choice(values, self.rows)
            else:
                data = np.random.choice(values, self.rows, p=probs)
        
        # decimal numbers (parameters: low, high)
        elif col_type in ("double", "decimals", "uniform"):
            low, high = part[1], part[2]
            data = np.random.uniform(low, high, self.rows)
            
        # percents (between 0 and 1) (parameters: alpha (pull towards 1), beta (pull towards 0)), make_percent (multiply by 100))
        elif col_type == "percent":
            alpha, beta_param, make_percent = part[1], part[2], part[3]
            data = np.random.beta(alpha, beta_param, self.rows)
            if make_percent == True:
                data *= 100
                
        ### true or false
        
        # boolean (parameters: none)
        elif col_type == "bool":
            data = np.random.choice([True, False], self.rows)

        # bernoulli (parameter: probability)
        elif col_type == "bernoulli":
            p = part[1]
            data = np.random.rand(self.rows) < p
            
        ### categorical
            
        # categorical (parameter: categories)
        elif col_type in ("category", "choice"):
            categories = part[1]
            data = np.random.choice(categories, self.rows)
        
        # weighted categorical (parameters: categories, probabilities-per-choice)
        elif col_type in ("category_prob", "category_weighted"):
            categories, probs = part[1], part[2]
            if not np.isclose(sum(probs), 1):
                raise ValueError("Probabilities must sum to 1.")
            data = np.random.choice(categories, self.rows, p=probs)
            
        ### letters
            
        # string (parameters: length, case [optional])
        elif col_type == "string":
            length = part[1]
            case = part[2] if len(part) > 2 else "both"
            if case == "lower":
                chars = string.ascii_lowercase
            elif case == "upper":
                chars = string.ascii_uppercase
            elif case == "both":
                chars = string.ascii_letters
            else:
                raise ValueError("case must be 'lower', 'upper', or 'both'")
            def rand_str():
                return "".join(np.random.choice(list(chars), length))
            data = [rand_str() for _ in range(self.rows)]
        
        
        ### identification
        
        # id column (parameters: starting value)
        elif col_type == "id":
            start = part[1] if len(part) > 1 else 1
            data = np.arange(start, start + self.rows)
        
        # prefix id (parameters: prefix, width, unique [optional])
        elif col_type == "prefix_id":
            prefix = str(part[1])
            width = int(part[2])
            unique = bool(part[3]) if len(part) > 3 else False
            if width <= 0:
                raise ValueError("width must be a positive integer")
            max_val = 10 ** width
            if unique:
                if self.rows > max_val:
                    raise ValueError(
                        f"Cannot generate {self.rows} unique IDs "
                        f"with width={width} (max={max_val})"
                    )
                nums = np.random.choice(max_val, size=self.rows, replace=False)
            else:
                nums = np.random.randint(0, max_val, size=self.rows)

            data = [
                prefix + str(num).zfill(width)
                for num in nums
            ]

        # alphanumeric id (parameters: length, unique [optional])
        elif col_type == "alphanumeric_id":
            length = part[1]
            unique = part[2] if len(part) > 2 else True
            chars = list(string.ascii_letters + string.digits)
            def rand_id():
                return "".join(np.random.choice(chars, size=length))
            if unique:
                ids = set()
                while len(ids) < self.rows:
                    ids.add(rand_id())
                data = list(ids)
            else:
                data = [rand_id() for _ in range(self.rows)]
        
        # names default (parameters: unique)
        elif col_type == "names":
            first_names = f_n
            last_names = l_n
            unique = part[1] if len(part) >1 else True
            if unique:
                names = [(f,l) for f in first_names for l in last_names]
                if self.rows > len(names):
                    raise ValueError("Not enough unique name combinations available.")
                index = np.random.choice(len(names), self.rows, replace=False)
                pairs = [names[i] for i in index]
            else:
                pairs = [
                    (np.random.choice(first_names), np.random.choice(last_names))
                    for _ in range(self.rows)
                ]
            self.df["first_name"] = [p[0] for p in pairs]
            self.df["last_name"]  = [p[1] for p in pairs]
            return self
        
        
        # email (parameters: domains)
        elif col_type == "email":
            domains = part[1] if len(part) > 1 else ["gmail.com", "yahoo.com", "outlook.com"]
            if "first_name" in self.df.columns and "last_name" in self.df.columns:
                first = self.df["first_name"].astype(str)
                last = self.df["last_name"].astype(str)
            else:
                first = pd.Series(np.random.choice(first_names, self.rows))
                last = pd.Series(np.random.choice(last_names, self.rows))
            first = first.str.lower().str.replace(r"[^a-z]", "", regex=True)
            last = last.str.lower().str.replace(r"[^a-z]", "", regex=True)
            base = first + "." + last
            domains_chosen = np.random.choice(domains, self.rows)
            data = (base + "@" + domains_chosen).tolist()

        
        # phone number (parameters: area_codes [optional], format [optional])
        elif col_type == "phone":
            if len(part) > 1:
                area_codes = part[1]
                if isinstance(area_codes, int):
                    area_codes = [area_codes]
            else:
                area_codes = [200, 201, 202, 212, 213, 305, 312, 404, 415, 510, 617, 650, 702, 718, 813, 917]
            format_type = part[2] if len(part) > 2 else "US"  # US, dots, dashes, plain
            def generate_phone():
                area_code = np.random.choice(area_codes)
                exchange = np.random.randint(200, 999)
                number = np.random.randint(1000, 9999)
                if format_type == "US":
                    return f"({area_code}) {exchange}-{number}"
                elif format_type == "dashes":
                    return f"{area_code}-{exchange}-{number}"
                elif format_type == "dots":
                    return f"{area_code}.{exchange}.{number}"
                elif format_type == "plain":
                    return f"{area_code}{exchange}{number}"
                else:
                    return f"({area_code}) {exchange}-{number}"
            data = [generate_phone() for _ in range(self.rows)]
        
        # state (parameters: abbreviated)
        elif col_type == "state":
            abrv = part[1] if len(part)>1 else False
            if abrv:
                states = [
                    "AL","AK","AZ","AR","CA","CO","CT","DE","FL","GA",
                    "HI","ID","IL","IN","IA","KS","KY","LA","ME","MD",
                    "MA","MI","MN","MS","MO","MT","NE","NV","NH","NJ",
                    "NM","NY","NC","ND","OH","OK","OR","PA","RI","SC",
                    "SD","TN","TX","UT","VT","VA","WA","WV","WI","WY"
                ]
            else:
                states = [
                    "Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware",
                    "Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky",
                    "Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi",
                    "Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico",
                    "New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania",
                    "Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont",
                    "Virginia","Washington","West Virginia","Wisconsin","Wyoming"
                ]

            data = np.random.choice(states, self.rows)
        
        # country (parameters: mode, weighted)
        elif col_type == "country":
            mode = part[1] if len(part) > 1 else "name"   # "name" or "iso"
            weighted = part[2] if len(part) > 2 else False
            country_map = {
                "US":"United States","CA":"Canada","MX":"Mexico",
                "BR":"Brazil","AR":"Argentina","CL":"Chile","CO":"Colombia","PE":"Peru","VE":"Venezuela",
                "GB":"United Kingdom","IE":"Ireland","FR":"France","DE":"Germany","ES":"Spain","PT":"Portugal",
                "IT":"Italy","NL":"Netherlands","BE":"Belgium","CH":"Switzerland","AT":"Austria",
                "SE":"Sweden","NO":"Norway","DK":"Denmark","FI":"Finland","PL":"Poland","CZ":"Czech Republic",
                "GR":"Greece","TR":"Turkey","UA":"Ukraine",
                "ZA":"South Africa","NG":"Nigeria","KE":"Kenya","EG":"Egypt","MA":"Morocco","GH":"Ghana",
                "CN":"China","IN":"India","JP":"Japan","KR":"South Korea","TH":"Thailand","VN":"Vietnam",
                "PH":"Philippines","ID":"Indonesia","MY":"Malaysia","SG":"Singapore",
                "PK":"Pakistan","BD":"Bangladesh","LK":"Sri Lanka",
                "SA":"Saudi Arabia","AE":"United Arab Emirates","IL":"Israel",
                "AU":"Australia","NZ":"New Zealand"
            }
            keys = list(country_map.keys())
            values = list(country_map.values())
            if weighted:
                weights = np.array([
                    0.20 if k == "US" else
                    0.08 if k in ["IN","CN"] else
                    0.05 if k in ["GB","DE","FR","JP"] else
                    0.01
                    for k in keys
                ])
                weights = weights / weights.sum()
                chosen = np.random.choice(keys, self.rows, p=weights)
            else:
                chosen = np.random.choice(keys, self.rows)
            data = chosen if mode == "iso" else [country_map[c] for c in chosen]
            
        # date of birth from age column (parameter: age column)
        elif col_type == "dob_from_age":
            age_col = part[1]
            today = pd.Timestamp.today().normalize()
            ages = self.df[age_col]
            # so everyone doesn't have the same birthday
            base_dob = today - pd.to_timedelta(ages * 365, unit="D")
            jitter = np.random.randint(0, 365, self.rows)
            data = base_dob - pd.to_timedelta(jitter, unit="D")

            
        # age from date of birth (parameters: dob column)
        elif col_type == "age_from_dob":
            dob_col = part[1]
            today = pd.Timestamp.today().normalize()
            dob = pd.to_datetime(self.df[dob_col], errors="coerce")
            had_birthday = (today.month > dob.dt.month) | (
                (today.month == dob.dt.month) & (today.day >= dob.dt.day)
            )
            data = (today.year - dob.dt.year - (~had_birthday).astype(int)).astype("Int64")

        # date (parameters: start_date, end_date)
        elif col_type == "date":
            start, end = pd.to_datetime(part[1]), pd.to_datetime(part[2])
            data = pd.to_datetime(
                np.random.randint(
                    start.value // 10**9,
                    end.value // 10**9,
                    self.rows
                ),
                unit="s"
            ).normalize()

        # datetime (parameters: start_date, end_date)
        elif col_type == "datetime":
            start, end = pd.to_datetime(part[1]), pd.to_datetime(part[2])
            data = pd.to_datetime(
                np.random.randint(
                    start.value // 10**9,
                    end.value // 10**9,
                    self.rows
                ),
                unit="s"
            )
            
        ### distributions

        # normal distribution (parameters: mean, standard_deviation)
        elif col_type == "normal":
            mean, sd = part[1], part[2]
            data = np.random.normal(mean, sd, self.rows)

        # lognormal distribution (parameters: mean, sigma)
        elif col_type == "lognormal":
            mean, sigma = part[1], part[2]
            data = np.random.lognormal(mean, sigma, self.rows)
            
        # normal distribution with min and max (parameters: mean, standard_deviation, min, max)
        elif col_type == "normal_clip":
            mean, sd, low, high = part[1], part[2], part[3], part[4]
            data = np.random.normal(mean, sd, self.rows)
            data = np.clip(data, low, high)

        # poisson distribution (parameter: lam)
        elif col_type == "poisson":
            lam = part[1]
            data = np.random.poisson(lam, self.rows)
            
        # beta distribution (parameter: alpha, beta, max)
        elif col_type == "beta":
            alpha, beta_param, max_val = part[1], part[2], part[3]
            data = np.random.beta(alpha, beta_param, self.rows) * max_val
        
        # exponential distribution (parameter: scale)
        elif col_type == "exponential":
            scale = part[1]
            data = np.random.exponential(scale, self.rows)

        # gamma distribution (parameters: shape, scale)
        elif col_type == "gamma":
            shape, scale = part[1], part[2]
            data = np.random.gamma(shape, scale, self.rows)
        
        # timeseries (parameters: start, slope, noise)
        elif col_type == "trend":
            start, slope, noise_sd = part[1], part[2], part[3]
            trend = start + slope * np.arange(self.rows)
            noise = np.random.normal(0, noise_sd, self.rows)
            data = trend + noise
            
        ### columns affected by other columns 
            
        # correlated column - linear (parameters: base_column, slope, standard_deviation)
        elif col_type == "correlated":
            base_col, slope, noise_sd = part[1], part[2], part[3]
            if base_col not in self.df.columns:
                raise ValueError(f"Base column '{base_col}' does not exist yet.")
            base = self.df[base_col]
            noise = np.random.normal(0, noise_sd, self.rows)
            data = slope * base + noise
        
        # conditional column (parameters: base_col, conditional_value, true_val, false_val)
        elif col_type == "conditional":
            condition_col, condition_val, true_val, false_val = part[1], part[2], part[3], part[4]
            data = np.where(self.df[condition_col] == condition_val, true_val, false_val)
        
        # computed column (parameters: function, dependent_columns)
        elif col_type == "computed":
            func = part[1]
            dependent_cols = part[2]
            data = func(self.df[dependent_cols])
            
        ### Analytics 
        
        ## rolling metrics 
    
        # rolling mean 
        elif col_type == "rolling_mean":
            base_col, window = part[1], part[2]
            min_p = part[3] if len(part) > 3 else window
            data = self.df[base_col].rolling(window, min_periods=min_p).mean()

        # rolling sum 
        elif col_type == "rolling_sum":
            base_col, window = part[1], part[2]
            min_p = part[3] if len(part) > 3 else window
            data = self.df[base_col].rolling(window, min_periods=min_p).sum()

        
        # rolling standard deviation 
        elif col_type == "rolling_std":
            base_col, window = part[1], part[2]
            min_p = part[3] if len(part) > 3 else window
            data = self.df[base_col].rolling(window, min_periods=min_p).std()

        # rolling max
        elif col_type == "rolling_max":
            base_col, window = part[1], part[2]
            min_p = part[3] if len(part) > 3 else window
            data = self.df[base_col].rolling(window, min_periods=min_p).max()
        
        # rolling min
        elif col_type == "rolling_min":
            base_col, window = part[1], part[2]
            min_p = part[3] if len(part) > 3 else window
            data = self.df[base_col].rolling(window, min_periods=min_p).min()

        ## other metrics
        
        # z-score (parameters: column to standardize)  
        elif col_type == "zscore":
            base_col = part[1]
            col = self.df[base_col]
            data = (col - col.mean()) / col.std()

        # bins (parameters: column to use, bins, labels for bins)
        elif col_type == "bin":
            base_col, bins, labels = part[1], part[2], part[3]
            data = pd.cut(self.df[base_col], bins=bins, labels=labels)
        
        # percent change (parameters: column to use)
        elif col_type == "pct_change":
            base_col = part[1]
            data = self.df[base_col].pct_change()


        
        #unknown column type
        else:
            raise ValueError(f"Column type is unknown: {col_type}")

        #series
        series = pd.Series(data)

        # apply missing values
        series = self.missing_add(series, m_percent)

        # apply rounding
        if round_num is not None:
            series = self.round_data(series, round_num)

        self.df[name] = series
        
        self.metadata.append({
            "column": name,
            "type": col_type,
            "parameters": part[1:-1] if isinstance(part[-1], dict) else part[1:],
            "missing_pct": m_percent,
            "rounding": round_num
        })
        
        return self
        
            
    #build dataframe
    def build(self):
        return self.df.copy()    