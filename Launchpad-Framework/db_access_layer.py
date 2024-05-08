import sqlite3
import logging

# Configure logging
logging.basicConfig(filename='db_access.log', level=logging.ERROR,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def connectDB():
    try:
        return sqlite3.connect('launchpad.db')
    except sqlite3.Error as e:
        logging.error(f"Error connecting to the database: {str(e)}")
        return None

def createUser(userID, username, avatar, isBot, joinedAt, warns=0, kicks=0, mutes=0, totalMessages=0, totalReactions=0):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO User (UserID, Username, Avatar, IsBot, JoinedAt, Warns, Kicks, Mutes, TotalMessages, TotalReactions)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (userID, username, avatar, isBot, joinedAt, warns, kicks, mutes, totalMessages, totalReactions))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating user: {str(e)}")
        finally:
            conn.close()

def readUser(userID):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM User WHERE UserID = ?", (userID,))
            user = cursor.fetchone()
            return user
        except sqlite3.Error as e:
            logging.error(f"Error reading user: {str(e)}")
        finally:
            conn.close()
    return None

def updateUser(userID, **kwargs):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            setClause = ', '.join(f"{k} = ?" for k in kwargs)
            values = list(kwargs.values()) + [user_id]
            cursor.execute(f"UPDATE User SET {setClause} WHERE UserID = ?", values)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error updating user: {str(e)}")
        finally:
            conn.close()

def deleteUser(userID):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM User WHERE UserID = ?", (userID,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting user: {str(e)}")
        finally:
            conn.close()

def createServer(serverID, name, icon, prefix, language, modRole, adminRole, muteRole, logChannel):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Server (ServerID, Name, Icon, Prefix, Language, ModRole, AdminRole, MuteRole, LogChannel)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?);
            """, (serverID, name, icon, prefix, language, modRole, adminRole, muteRole, logChannel))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating server: {str(e)}")
        finally:
            conn.close()

def readServer(serverID):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Server WHERE ServerID = ?", (serverID,))
            server = cursor.fetchone()
            return server
        except sqlite3.Error as e:
            logging.error(f"Error reading server: {str(e)}")
        finally:
            conn.close()
    return None

def updateServer(serverID, **kwargs):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            setClause = ', '.join(f"{k} = ?" for k in kwargs)
            values = list(kwargs.values()) + [server_id]
            cursor.execute(f"UPDATE Server SET {setClause} WHERE ServerID = ?", values)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error updating server: {str(e)}")
        finally:
            conn.close()

def deleteServer(serverID):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Server WHERE ServerID = ?", (serverID,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting server: {str(e)}")
        finally:
            conn.close()

def createReminder(serverID, userID, reminderText, remindAt, reminded=False):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Reminders (ServerID, UserID, ReminderText, RemindAt, Reminded)
                VALUES (?, ?, ?, ?, ?);
            """, (serverID, userID, reminderText, remindAt, reminded))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating reminder: {str(e)}")
        finally:
            conn.close()

def readReminder(reminderID):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Reminders WHERE ReminderID = ?", (reminderID,))
            reminder = cursor.fetchone()
            return reminder
        except sqlite3.Error as e:
            logging.error(f"Error reading reminder: {str(e)}")
        finally:
            conn.close()
    return None

def updateReminder(reminderID, **kwargs):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            setClause = ', '.join(f"{k} = ?" for k in kwargs)
            values = list(kwargs.values()) + [reminder_id]
            cursor.execute(f"UPDATE Reminders SET {setClause} WHERE ReminderID = ?", values)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error updating reminder: {str(e)}")
        finally:
            conn.close()

def deleteReminder(reminder_id):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Reminders WHERE ReminderID = ?", (reminderID,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting reminder: {str(e)}")
        finally:
            conn.close()

def createModeration(serverID, userID, action, reason, moderatorID, createdAt):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Moderations (ServerID, UserID, Action, Reason, ModeratorID, CreatedAt)
                VALUES (?, ?, ?, ?, ?, ?);
            """, (serverID, userID, action, reason, moderatorID, createdAt))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating moderation: {str(e)}")
        finally:
            conn.close()

def readModeration(moderationID):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Moderations WHERE ModerationID = ?", (moderationID,))
            moderation = cursor.fetchone()
            return moderation
        except sqlite3.Error as e:
            logging.error(f"Error reading moderation: {str(e)}")
        finally:
            conn.close()
    return None

def updateModeration(moderationID, **kwargs):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            setClause = ', '.join(f"{k} = ?" for k in kwargs)
            values = list(kwargs.values()) + [moderationID]
            cursor.execute(f"UPDATE Moderations SET {setClause} WHERE ModerationID = ?", values)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error updating moderation: {str(e)}")
        finally:
            conn.close()

def deleteModeration(moderationID):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Moderations WHERE ModerationID = ?", (moderationID,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting moderation: {str(e)}")
        finally:
            conn.close()

def createSuggestion(serverID, userID, suggestionText, messageID, createdAt, status='pending', resolvedBy=None, resolvedAt=None):
    conn = connect_db()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Suggestions (ServerID, UserID, Suggestion, MessageID, CreatedAt, Status, ResolvedBy, ResolvedAt)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?);
            """, (serverID, userID, suggestionText, messageID, createdAt, status, resolvedBy, resolvedAt))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating suggestion: {str(e)}")
        finally:
            conn.close()

def readSuggestion(suggestionID):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Suggestions WHERE SuggestionID = ?", (suggestionID,))
            suggestion = cursor.fetchone()
            return suggestion
        except sqlite3.Error as e:
            logging.error(f"Error reading suggestion: {str(e)}")
        finally:
            conn.close()
    return None

def updateSuggestion(suggestionID, **kwargs):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            setClause = ', '.join(f"{k} = ?" for k in kwargs)
            values = list(kwargs.values()) + [suggestionID]
            cursor.execute(f"UPDATE Suggestions SET {set_clause} WHERE SuggestionID = ?", values)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error updating suggestion: {str(e)}")
        finally:
            conn.close()

def deleteSuggestion(suggestionID):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Suggestions WHERE SuggestionID = ?", (suggestionID,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting suggestion: {str(e)}")
        finally:
            conn.close()

def createStarboard(serverID, channelID, minStars=3):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO Starboards (ServerID, ChannelID, MinStars)
                VALUES (?, ?, ?);
            """, (serverID, channelID, minStars))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error creating starboard: {str(e)}")
        finally:
            conn.close()

def readStarboard(starID):
    conn = connectDB()
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

def updateStarboard(starID, **kwargs):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            setClause = ', '.join(f"{k} = ?" for k in kwargs)
            values = list(kwargs.values()) + [star_id]
            cursor.execute(f"UPDATE Starboards SET {setClause} WHERE StarID = ?", values)
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error updating starboard: {str(e)}")
        finally:
            conn.close()

def deleteStarboard(starID):
    conn = connectDB()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM Starboards WHERE StarID = ?", (star_id,))
            conn.commit()
        except sqlite3.Error as e:
            logging.error(f"Error deleting starboard: {str(e)}")
        finally:
            conn.close()