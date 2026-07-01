from scrapers.booking.scraper import obtener_alojamiento

alojamiento = obtener_alojamiento(
    url="https://www.booking.com/hotel/ar/tierra-de-mestizos.es.html?aid=2311236&label=es-ar-booking-desktop-MRRNwpxuLSY8eNXQ7griKwS652829001343%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-65526620%3Alp9185662%3Ali%3Adec%3Adm&sid=051d6491ff9af3f06e8868c69b5fbfc8&all_sr_blocks=315195405_123577548_2_0_0&checkin=2027-01-04&checkout=2027-01-09&dest_id=-1018998&dest_type=city&dist=0&group_adults=2&group_children=0&hapos=1&highlighted_blocks=315195405_123577548_2_0_0&hpos=1&matching_block_id=315195405_123577548_2_0_0&no_rooms=1&req_adults=2&req_children=0&room1=A%2CA&sb_price_type=total&sr_order=popularity&sr_pri_blocks=315195405_123577548_2_0_0__27500&srepoch=1782593822&srpvid=42a3934e53a700cd&type=total&ucfs=1&",
    check_in="2026-07-03",
    check_out="2026-07-05",
    viajeros=3,
)

print(alojamiento)
