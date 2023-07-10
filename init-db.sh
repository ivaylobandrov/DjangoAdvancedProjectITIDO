psql -U $POSTGRES_USER -c "CREATE DATABASE csvdb"

psql -U $POSTGRES_USER -d $POSTGRES_DB -c "CREATE TABLE pricesandquantities(date DATE, price_bgn_mwh decimal, volume_mwh decimal)"
psql -U $POSTGRES_USER -d $POSTGRES_DB -c "CREATE TABLE blockproduct(date DATE, base_price_bgn_mwh decimal, peak_price_bgn_mwh decimal, off_peak_price_bgn_mwh decimal)"
