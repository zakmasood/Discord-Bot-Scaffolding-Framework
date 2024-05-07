# Manobloom Framework for Discord.py Bot Applications

This Discord bot is built with Python and the discord.py library, and it leverages SQLite, a lightweight and serverless database management system, to store and manage its data. The use of SQLite provides several advantages over traditional databases, making this bot stand out from other Discord bots.

## Database Schema

The bot's data is organized into several tables in the SQLite database, each serving a specific purpose:

1. **User**: Stores user information such as ID, username, avatar, bot status, join timestamp, and various moderation counts.
2. **Server**: Contains server-specific settings like name, icon, prefix, language, and various role and channel IDs for moderation purposes.
3. **Moderations**: Keeps track of moderation actions (warnings, kicks, mutes, and bans) with details like server ID, user ID, action type, reason, moderator ID, and timestamp.
4. **Starboards**: Stores starboard configurations, including the server ID, channel ID, and minimum stars required for a message to be reposted.
5. **Reminders**: Stores reminders set by users, including server ID, user ID, reminder text, remind timestamp, and a flag indicating if the reminder has been sent.
6. **Suggestions**: Maintains server suggestions submitted by users, including server ID, user ID, suggestion text, message ID, creation timestamp, status, and details about who resolved the suggestion and when.

This schema design ensures data integrity, efficient querying, and scalability for the bot's various features, you can add more as you see fit!

## Benefits of Using SQLite

By leveraging SQLite as the database engine, this Discord bot gains several advantages:

1. **Serverless**: SQLite databases are file-based, eliminating the need for a separate database server or server configuration.
2. **Lightweight**: SQLite has a small footprint, making it easy to distribute and deploy the bot across different environments.
3. **Cross-Platform**: SQLite is compatible with various operating systems, ensuring the bot can run seamlessly on different platforms.
4. **Embedded**: SQLite can be embedded directly into the application, simplifying the deployment process and reducing dependencies.
5. **Atomic Transactions**: SQLite provides robust transaction support, ensuring data integrity and consistency even in case of crashes or power failures.
6. **Performance**: For small to medium-sized applications, SQLite can offer comparable or better performance than traditional client-server database engines.

By choosing SQLite, this Discord bot achieves a balance between functionality and simplicity, making it a robust and efficient solution for managing moderation and utility features in Discord servers.

## Installation and Usage

[Installation and usage instructions go here]

## Contributing

Contributions are welcome! If you find any issues or have suggestions for new features, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).
