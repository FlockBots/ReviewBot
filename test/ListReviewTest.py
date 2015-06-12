from modules import list_reviews
from modules import ReviewBase
from test import testinfo
rb = ReviewBase(testinfo['database_filename'])

def select_test():
    reviews = list_reviews._get_reviews(user='texacer', review_db=rb)
    reply = list_reviews._create_review_list(reviews)
    return reply == "* [Maker's Mark Cask Strength: a review](http://www.reddit.com/r/bourbon/comments/325igk/makers_mark_cask_strength_a_review/)\n* [Four Roses /r/bourbon selection OBSF: a review](http://www.reddit.com/r/bourbon/comments/2x11qs/four_roses_rbourbon_selection_obsf_a_review/)\n* [Bunnahabhain 25 year: a review](http://www.reddit.com/r/Scotch/comments/2svb0s/bunnahabhain_25_year_a_review/)\n* [Aberlour DARKNESS 20 year old Oloroso: a review](http://www.reddit.com/r/Scotch/comments/2svcb2/aberlour_darkness_20_year_old_oloroso_a_review/)\n* [Glenkinchie 20 year old Cask Strength: a review](http://www.reddit.com/r/Scotch/comments/2pqv9j/glenkinchie_20_year_old_cask_strength_a_review/)\n* [Buffalo Trace Experimental Collection Wheat 90: a review](http://www.reddit.com/r/bourbon/comments/2orzmx/buffalo_trace_experimental_collection_wheat_90_a/)\n* [Glen Breton Ice 17 year: a review](http://www.reddit.com/r/worldwhisky/comments/2nigiu/glen_breton_ice_17_year_a_review/)\n* [Laphroaig 20 year old 1993 Soveriegn: a review](http://www.reddit.com/r/Scotch/comments/2mxz0z/laphroaig_20_year_old_1993_soveriegn_a_review/)\n* [Old Medley 12 year old: a review](http://www.reddit.com/r/bourbon/comments/2lamyx/old_medley_12_year_old_a_review/)\n* [Ardbeg 21 year old 1992 Sovereign: a review](http://www.reddit.com/r/Scotch/comments/2kbh1v/ardbeg_21_year_old_1992_sovereign_a_review/)\n\n"


def select_bottle_test():
    review_gen = list_reviews._get_reviews(user='texacer', bottle='johnnie', review_db=rb)
    reply = list_reviews._create_review_list(review_gen)
    return reply == '* [Johnnie Walker XR 21 year old: a review](http://www.reddit.com/r/Scotch/comments/2dcdg4/johnnie_walker_xr_21_year_old_a_review/)\n* [Johnnie Walker Gold Label Centenary Blend: a review](http://www.reddit.com/r/Scotch/comments/1hxynr/johnnie_walker_gold_label_centenary_blend_a_review/)\n* [Johnnie Walker Red Label: a review](http://www.reddit.com/r/Scotch/comments/12j0g5/johnnie_walker_red_label_a_review/)\n* [Johnnie Walker Green Label 15: a review](http://www.reddit.com/r/Scotch/comments/t5chk/johnnie_walker_green_label_15_a_review/)\n* [Johnnie Walker King George V](http://www.reddit.com/r/WhiskeyReviews/comments/o3pa5/johnnie_walker_king_george_v/)\n* [Johnnie Walker Double Black: a review](http://www.reddit.com/r/WhiskeyReviews/comments/mh2cv/johnnie_walker_double_black_a_review/)\n* [Johnnie Walker Black Label](http://www.reddit.com/r/WhiskeyReviews/comments/kdy1k/johnnie_walker_black_label/)\n* [Review:  Johnnie Walker Blue Label](http://www.reddit.com/r/Scotch/comments/evndl/review_johnnie_walker_blue_label/)\n* [Dalwhinnie 15](http://www.reddit.com/r/WhiskeyReviews/comments/n1ebu/dalwhinnie_15/)\n\n'


def select_subreddit_test():
    reviews = list_reviews._get_reviews(user='texacer', subreddit='WorldWhisky', review_db = rb)
    reply = list_reviews._create_review_list(reviews)
    return reply == '* [Glen Breton Ice 17 year: a review](http://www.reddit.com/r/worldwhisky/comments/2nigiu/glen_breton_ice_17_year_a_review/)\n* [Nikka Taketsuru 17 year: a review](http://www.reddit.com/r/worldwhisky/comments/2051l8/nikka_taketsuru_17_year_a_review/)\n* [Tullamore Dew Phoenix Limited Edition Cask Strength: a review](http://www.reddit.com/r/worldwhisky/comments/1uhjq5/tullamore_dew_phoenix_limited_edition_cask/)\n* [Amrut Portonova: a review](http://www.reddit.com/r/worldwhisky/comments/1u5x7w/amrut_portonova_a_review/)\n* [Heartwood Convict Release: a review](http://www.reddit.com/r/worldwhisky/comments/1kbef8/heartwood_convict_release_a_review/)\n* [Redbreast 15 year old: a review](http://www.reddit.com/r/worldwhisky/comments/1fdfy9/redbreast_15_year_old_a_review/)\n* [Alberta Premium Dark Horse: review](http://www.reddit.com/r/worldwhisky/comments/16gzv5/alberta_premium_dark_horse_review/)\n* [Forty Creek Port Wood: a review](http://www.reddit.com/r/worldwhisky/comments/169w0x/forty_creek_port_wood_a_review/)\n* [Forty Creek Confederation Oak: a review](http://www.reddit.com/r/worldwhisky/comments/15v609/forty_creek_confederation_oak_a_review/)\n* [Alberta Premium: a review](http://www.reddit.com/r/worldwhisky/comments/15p5me/alberta_premium_a_review/)\n\n'