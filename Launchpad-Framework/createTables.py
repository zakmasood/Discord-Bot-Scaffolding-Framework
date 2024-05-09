import sqlite3

def create_manobloom_tables():
    # Create a new SQLite database
    connection = sqlite3.connect('launchpad.db')
    
    # Create a cursor object using the cursor() method
    cursor = connection.cursor()
    
    # SQL DDL statements
    ddlStatements = """
    -- User Table
    CREATE TABLE IF NOT EXISTS User (
        UserID BIGINT PRIMARY KEY,
        Username VARCHAR(32) NOT NULL,
        Avatar VARCHAR(64),
        IsBot BOOLEAN DEFAULT FALSE NOT NULL,
        JoinedAt TIMESTAMP NOT NULL,
        Warns INT DEFAULT 0 NOT NULL,
        Kicks INT DEFAULT 0 NOT NULL,
        Mutes INT DEFAULT 0 NOT NULL,
        TotalMessages INT DEFAULT 0 NOT NULL,
        TotalReactions INT DEFAULT 0 NOT NULL
    );

    -- Server Table
    CREATE TABLE IF NOT EXISTS Server (
        ServerID BIGINT PRIMARY KEY,
        Name VARCHAR(100) NOT NULL,
        Icon VARCHAR(64),
        Prefix VARCHAR(5) DEFAULT '!' NOT NULL,
        Language VARCHAR(5) DEFAULT 'en' NOT NULL,
        ModRole BIGINT NOT NULL,
        AdminRole BIGINT NOT NULL,
        MuteRole BIGINT NOT NULL,
        LogChannel BIGINT NOT NULL
    );

    -- Reminders Table
    CREATE TABLE IF NOT EXISTS Reminders (
        ReminderID INTEGER PRIMARY KEY AUTOINCREMENT,
        ServerID BIGINT NOT NULL REFERENCES Server(ServerID),
        UserID BIGINT NOT NULL REFERENCES User(UserID),
        ReminderText TEXT NOT NULL,
        RemindAt TIMESTAMP NOT NULL,
        Reminded BOOLEAN DEFAULT FALSE NOT NULL
    );

    -- Moderations Table
    CREATE TABLE IF NOT EXISTS Moderations (
        ModerationID INTEGER PRIMARY KEY AUTOINCREMENT,
        ServerID BIGINT NOT NULL REFERENCES Server(ServerID),
        UserID VARCHAR(64) NOT NULL REFERENCES User(UserID),
        Action VARCHAR(10) NOT NULL, -- WARN, KICK, MUTE
        Reason TEXT,
        ModeratorID BIGINT NOT NULL REFERENCES User(UserID),
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL
    );

    -- Suggestions Table
    CREATE TABLE IF NOT EXISTS Suggestions (
        SuggestionID INTEGER PRIMARY KEY AUTOINCREMENT,
        ServerID BIGINT NOT NULL REFERENCES Server(ServerID),
        UserID VARCHAR(64) NOT NULL REFERENCES User(UserID),
        Suggestion TEXT NOT NULL,
        MessageID BIGINT,
        CreatedAt TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
        Status VARCHAR(10) DEFAULT 'pending' NOT NULL,
        ResolvedBy BIGINT,
        ResolvedAt TIMESTAMP
    );

    -- Starboards Table
    CREATE TABLE IF NOT EXISTS Starboards (
        StarID INTEGER PRIMARY KEY AUTOINCREMENT,
        ServerID BIGINT NOT NULL REFERENCES Server(ServerID),
        ChannelID BIGINT NOT NULL,
        MinStars INT DEFAULT 3 NOT NULL
    );
    """
    
    # Executing the DDL statements
    cursor.executescript(ddlStatements)
    
    # Committing the changes
    connection.commit()
    
    # Closing the connection
    connection.close()