# Overview

This is a Discord bot application built using discord.py library. The bot implements slash commands for server moderation and communication, specifically designed to work with a single Discord server. The primary functionality includes a test command and a direct message (DM) command that allows staff members to send messages to users.

# User Preferences

Preferred communication style: Simple, everyday language.

# System Architecture

## Bot Framework
- **Technology**: discord.py with slash commands (app_commands)
- **Design Pattern**: Event-driven architecture using Discord.py's client-based model
- **Rationale**: Slash commands provide a modern, user-friendly interface within Discord, replacing traditional prefix-based commands. The app_commands framework ensures better discoverability and validation.

## Command Structure
- **Guild-Scoped Commands**: Commands are registered to a specific server (guild ID: 1346919403689611314)
- **Rationale**: Guild-scoped commands sync faster than global commands and are appropriate for single-server bots. This reduces command propagation delay from hours to seconds.
- **Permission Model**: Role-based access control using Discord's built-in permission system (manage_messages permission)

## Authentication & Authorization
- **Bot Authentication**: Token-based authentication via environment variables
- **User Authorization**: Permission checks using Discord's guild_permissions (manage_messages for staff commands)
- **Rationale**: Leverages Discord's native permission system rather than implementing custom role management, reducing complexity and maintaining consistency with Discord's UX.

## Command Synchronization
- **Sync Strategy**: One-time sync on bot ready event with sync flag to prevent duplicate syncs
- **Rationale**: Prevents excessive API calls while ensuring commands are registered when the bot starts

## Error Handling
- **DM Failures**: Catches discord.Forbidden exceptions when users have DMs disabled
- **Note**: Error handling appears incomplete in the provided code (dm_command function is truncated)

# External Dependencies

## Discord API
- **Library**: discord.py (v2.x based on app_commands usage)
- **Purpose**: Primary interface for Discord bot functionality, slash commands, and messaging
- **Integration Points**: Command registration, user interactions, message sending, permission checking

## Environment Management
- **Library**: python-dotenv
- **Purpose**: Manages sensitive configuration (bot token) via .env file
- **Security**: Keeps credentials out of source code

## Required Environment Variables
- Bot token (loaded via dotenv, variable name not shown in code)

## Discord Server Configuration
- **Server ID**: Hardcoded guild ID (1346919403689611314)
- **Consideration**: May need refactoring for multi-server support in the future