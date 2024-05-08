import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='db_access.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def connect_db():
    try:
        return sqlite3.connect('launchpad.db')
    except sqlite3.Error as e:
        logging.error(f"Error connecting to the database: {str(e)}")
        return None

def create_user(user_id, username, avatar, is_bot, joined_at, warns=0, kicks=0, mutes=0, total_messages=0, total_reactions=0):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO User (UserID, Username, Avatar, IsBot, JoinedAt, Warns, Kicks, Mutes, TotalMessages, TotalReactions)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (user_id, username, avatar, is_bot, joined_at, warns, kicks, mutes, total_messages, total_reactions))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating user: {str(e)}")
        finally:
            conn.close()

def read_user(user_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM User WHERE UserID = ?", (user_id,))
            user = cursor.fetchone()
            return user
        except sqlite3.Error as e:
            logging.error(f"Error reading user: {str(e)}")
        finally:
            conn.close()
    return None

def update_user(user_id, **kwargs):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            set_clause = ', '.join(f"{k} = ?" for k in kwargs)
            values = list(kwargs.values()) + [user_id]
            cursor.execute(f"UPDATE User SET {set_clause} WHERE UserID = ?", values)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error updating user: {str(e)}")
        finally:
            conn.close()

def delete_user(user_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM User WHERE UserID = ?", (user_id,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting user: {str(e)}")
        finally:
            conn.close()

def create_server(server_id, name, icon, prefix, language, mod_role, admin_role, mute_role, log_channel):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Server (ServerID, Name, Icon, Prefix, Language, ModRole, AdminRole, MuteRole, LogChannel)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (server_id, name, icon, prefix, language, mod_role, admin_role, mute_role, log_channel))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating server: {str(e)}")
        finally:
            conn.close()

def read_server(server_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Server WHERE ServerID = ?", (server_id,))
            server = cursor.fetchone()
            return server
        except sqlite3.Error as e:
            logging.error(f"Error reading server: {str(e)}")
        finally:
            conn.close()
    return None

def update_server(server_id, **kwargs):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            set_clause = ', '.join(f"{k} = ?" for k in kwargs)
            values = list(kwargs.values()) + [server_id]
            cursor.execute(f"UPDATE Server SET {set_clause} WHERE ServerID = ?", values)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error updating server: {str(e)}")
        finally:
            conn.close()

def delete_server(server_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Server WHERE ServerID = ?", (server_id,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting server: {str(e)}")
        finally:
            conn.close()

def create_reminder(server_id, user_id, reminder_text, remind_at, reminded=False):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Reminders (ServerID, UserID, ReminderText, RemindAt, Reminded)
                VALUES (?, ?, ?, ?, ?);
            """, (server_id, user_id, reminder_text, remind_at, reminded))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating reminder: {str(e)}")
        finally:
            conn.close()

def read_reminder(reminder_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Reminders WHERE ReminderID = ?", (reminder_id,))
            reminder = cursor.fetchone()
            return reminder
        except sqlite3.Error as e:
            logging.error(f"Error reading reminder: {str(e)}")
        finally:
            conn.close()
    return None

def update_reminder(reminder_id, **kwargs):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            set_clause = ', '.join(f"{k} = ?" for k in kwargs)
            values = list(kwargs.values()) + [reminder_id]
            cursor.execute(f"UPDATE Reminders SET {set_clause} WHERE ReminderID = ?", values)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error updating reminder: {str(e)}")
        finally:
            conn.close()

def delete_reminder(reminder_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Reminders WHERE ReminderID = ?", (reminder_id,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting reminder: {str(e)}")
        finally:
            conn.close()

def create_moderation(server_id, user_id, action, reason, moderator_id, created_at):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Moderations (ServerID, UserID, Action, Reason, ModeratorID, CreatedAt)
                VALUES (?, ?, ?, ?, ?, ?);
            """, (server_id, user_id, action, reason, moderator_id, created_at))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating moderation: {str(e)}")
        finally:
            conn.close()

def read_moderation(moderation_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Moderations WHERE ModerationID = ?", (moderation_id,))
            moderation = cursor.fetchone()
            return moderation
        except sqlite3.Error as e:
            logging.error(f"Error reading moderation: {str(e)}")
        finally:
            conn.close()
    return None

def update_moderation(moderation_id, **kwargs):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            set_clause = ', '.join(f"{k} = ?" for k in kwargs)
            values = list(kwargs.values()) + [moderation_id]
            cursor.execute(f"UPDATE Moderations SET {set_clause} WHERE ModerationID = ?", values)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error updating moderation: {str(e)}")
        finally:
            conn.close()

def delete_moderation(moderation_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Moderations WHERE ModerationID = ?", (moderation_id,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting moderation: {str(e)}")
        finally:
            conn.close()

def create_suggestion(server_id, user_id, suggestion_text, message_id, created_at, status='pending', resolved_by=None, resolved_at=None):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Suggestions (ServerID, UserID, Suggestion, MessageID, CreatedAt, Status, ResolvedBy, ResolvedAt)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """, (server_id, user_id, suggestion_text, message_id, created_at, status, resolved_by, resolved_at))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating suggestion: {str(e)}")
        finally:
            conn.close()

def read_suggestion(suggestion_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Suggestions WHERE SuggestionID = ?", (suggestion_id,))
            suggestion = cursor.fetchone()
            return suggestion
        except sqlite3.Error as e:
            logging.error(f"Error reading suggestion: {str(e)}")
        finally:
            conn.close()
    return None

def update_suggestion(suggestion_id, **kwargs):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            set_clause = ', '.join(f"{k} = ?" for k in kwargs)
            values = list(kwargs.values()) + [suggestion_id]
            cursor.execute(f"UPDATE Suggestions SET {set_clause} WHERE SuggestionID = ?", values)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error updating suggestion: {str(e)}")
        finally:
            conn.close()

def delete_suggestion(suggestion_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Suggestions WHERE SuggestionID = ?", (suggestion_id,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting suggestion: {str(e)}")
        finally:
            conn.close()

def create_starboard(server_id, channel_id, min_stars=3):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Starboards (ServerID, ChannelID, MinStars)
                VALUES (?, ?, ?);
            """, (server_id, channel_id, min_stars))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating starboard: {str(e)}")
        finally:
            conn.close()

def read_starboard(star_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Starboards WHERE StarID = ?", (star_id,))
            starboard = cursor.fetchone()
            return starboard
        except sqlite3.Error as e:
            logging.error(f"Error reading starboard: {str(e)}")
        finally:
            conn.close()
    return None

def update_starboard(star_id, **kwargs):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            set_clause = ', '.join(f"{k} = ?" for k in kwargs)
            values = list(kwargs.values()) + [star_id]
            cursor.execute(f"UPDATE Starboards SET {set_clause} WHERE StarID = ?", values)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error updating starboard: {str(e)}")
        finally:
            conn.close()

def delete_starboard(star_id):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Starboards WHERE StarID = ?", (star_id,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting starboard: {str(e)}")
        finally:
            conn.close()