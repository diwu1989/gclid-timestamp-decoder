from gclid_timestamp_decoder.decode import get_timestamp_from_gclid, decode_gclid

gclids = [
    "EAIaIQobChMIl4Pcqteb8gIV9Al9Ch1BmgjCEAAYASAAEgLCtfD_BwE",
    "EAIaIQobChMIsOuZ1NWb8gIV0TytBh1EUQfSEAAYASAAEgJ2l_D_BwE"
]

for gclid in gclids:
    print(get_timestamp_from_gclid(gclid))
    print(decode_gclid(gclid))
