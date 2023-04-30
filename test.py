from chessdotcom import (get_player_profile, get_player_stats, get_current_daily_puzzle)

# test getting user information:
print('***************************User Information**************************************')

user_info_response = get_player_profile("suleymankiani")
# print(type(user_info_response))
# print('')
# print(user_info_response._parse_response)
# print('')
# print(user_info_response._create_json_attr)
username = user_info_response.player.username
user_id = user_info_response.player.player_id
print("Username:", username)
print("User ID:", user_id)

print('***************************Statistics**************************************')
# test getting user statistics
user_stats_response = get_player_stats("suleymankiani")

# print(user_stats_response._parse_response)
user_bullet_rating = user_stats_response.stats.chess_bullet.last.rating
user_best_bullet_rating = user_stats_response.stats.chess_bullet.best.rating

user_blitz_rating = user_stats_response.stats.chess_blitz.last.rating
user_best_blitz_rating = user_stats_response.stats.chess_blitz.best.rating

user_rapid_rating = user_stats_response.stats.chess_rapid.last.rating
user_best_rapid_rating = user_stats_response.stats.chess_rapid.best.rating

print("Bullet Rating:", user_bullet_rating)
print("Best Bullet Rating:", user_best_bullet_rating)

print("Blitz Rating:", user_blitz_rating)
print("Best Blitz Rating:", user_best_blitz_rating)

print("Rapid Rating:", user_rapid_rating)
print("Best Bullet Rating:", user_best_rapid_rating)





print('')

# test getting daily puzzle:
print('******************************Daily Puzzle***********************************')

# daily_puzzle_test = get_current_daily_puzzle()
# print(daily_puzzle_test._parse_response)



# player_name = response.json['player']['name']
# print(player_name)

# player_name = response.player.name
# print(player_name)



