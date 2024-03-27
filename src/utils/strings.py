    
    
#     # print_sdk(sdk, **style['default'])
#     print_sdk(sdk, **style['simple_margin'])
#     print_sdk(sdk, **style['ocean'])
    
# def print_unicode_characters_columns(start=32, end=1000, column_count=5):
#     """
#     Print Unicode characters and their codes from 'start' to 'end' in columns.
    
#     :param start: Starting Unicode code point (inclusive).
#     :param end: Ending Unicode code point (exclusive).
#     :param column_count: Number of columns for the output.
#     """
#     print("Unicode Characters and their codes:")
#     for i in range(start, end):
#         try:
#             # Calculate padding for alignment
#             end_char = '\n' if (i - start) % column_count == column_count - 1 else '\t'
#             print(f"{chr(i)}: {i}", end=end_char)
#         except UnicodeEncodeError:
#             pass  # Skip characters not supported by the terminal's encoding
#     print()  # Ensure there's a newline at the end

# # print_unicode_characters_columns(32, 140000)

# # Character from the Basic Multilingual Plane (BMP)
# char_bmp = '\u263A'  # Smiley face character
# print(f'BMP Character (U+263A): {char_bmp}')

# # Character from a Supplementary Plane
# char_supplementary = '\U0001F600'  # Grinning face emoji
# print(f'Supplementary Plane Character (U+1F600): {char_supplementary}')

# # # List of some common emoji code points
# # emoji_code_points = [
# #     0x1F600,  # 😀 Grinning Face
# #     0x1F601,  # 😁 Beaming Face With Smiling Eyes
# #     0x1F602,  # 😂 Face With Tears of Joy
# #     0x1F603,  # 😃 Smiling Face With Open Mouth
# #     0x1F604,  # 😄 Smiling Face With Open Mouth & Smiling Eyes
# #     0x1F605,  # 😅 Smiling Face With Open Mouth & Cold Sweat
# #     0x1F606,  # 😆 Smiling Face With Open Mouth & Closed Eyes
# #     0x1F607,  # 😇 Smiling Face With Halo
# #     # Add more emojis as desired
# # ]

# # # Print each emoji with its description
# # for code_point in emoji_code_points:
# #     emoji_char = chr(code_point)
# #     print(f"{emoji_char}", end=' ')
# # print()  # Newline after printing all emojis

# # def print_emojis(start, end):
# #     print("Emoji range:")
# #     for code_point in range(start, end):
# #         try:
# #             print(chr(code_point), end=' ')
# #         except UnicodeEncodeError:
# #             # Some code points may not be valid depending on the Python version and environment
# #             pass
# #     print()  # Newline at the end

# # # Example ranges (these ranges are approximate and may include non-emoji characters)
# # # Adjust these ranges according to the specific emojis you are interested in
# # smileys_emotion_start = 0x1F600
# # smileys_emotion_end = 0x1F64F  # End is exclusive

# # people_body_start = 0x1F466
# # people_body_end = 0x1F487  # End is exclusive

# # print_emojis(smileys_emotion_start, smileys_emotion_end)
# # print_emojis(people_body_start, people_body_end)



# horizontal_line = '\u2500'
# vertical_line = '\u2502'
# cross = '\u253C'
# top_left_corner = '\u250C'
# top_right_corner = '\u2510'
# bottom_left_corner = '\u2514'
# bottom_right_corner = '\u2518'
# t_down = '\u252C'
# t_up = '\u2534'
# t_left = '\u2524'
# t_right = '\u251C'
# print("├──────┼───────┼──────┤")
# print("└──────┴───────┴──────┘")


# # Print all printable ASCII characters
#     for i in range(32, 127):
#         print(chr(i), end=' ')
#     print()  # Move to a new line at the end
    
#     # Print all extended ASCII characters (might vary by terminal encoding)
#     for i in range(128, 256):
#         print(chr(i), end=' ')
#     print()  # Move to a new line at the end
    
#     # Print a range of Unicode characters
#     for i in range(1024):
#         try:
#             print(chr(i), end=' ')
#         except UnicodeEncodeError:
#             pass  # Some characters may not be supported in the terminal's encoding
#     print()  # Move to a new line at the end
    