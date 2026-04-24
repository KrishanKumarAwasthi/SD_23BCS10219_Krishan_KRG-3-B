# VYBE - High-Level Design (HLD) Document

**Project Name:** VYBE - Social Media Platform  
**Version:** 1.0.0  
**Last Updated:** April 2026  
**Document Status:** Final

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [System Overview](#system-overview)
3. [Architecture Overview](#architecture-overview)
4. [Technology Stack](#technology-stack)
5. [System Components](#system-components)
6. [Data Models & Entity Relationships](#data-models--entity-relationships)
7. [Key Workflows & Features](#key-workflows--features)
8. [Real-time Communication Architecture](#real-time-communication-architecture)
9. [API Architecture](#api-architecture)
10. [Security Architecture](#security-architecture)
11. [Scalability & Performance](#scalability--performance)
12. [Deployment Architecture](#deployment-architecture)
13. [Error Handling & Monitoring](#error-handling--monitoring)
14. [Future Enhancements](#future-enhancements)

---

## Executive Summary

VYBE is a modern, full-stack social media platform designed to enable users to connect, share content, and communicate in real-time. The system combines traditional RESTful APIs for CRUD operations with WebSocket technology for real-time messaging and online status tracking. The architecture follows a three-tier model with clear separation between presentation, business logic, and data layers.

### Key Objectives
- Enable seamless social connection and content sharing
- Provide real-time messaging and notifications
- Support multi-media content (images, videos, stories)
- Ensure scalable and maintainable codebase
- Deliver responsive, modern user experience

---

## System Overview

### What is VYBE?
VYBE is a comprehensive social networking platform that combines features from popular social media applications. It provides users with multiple ways to interact, including:

- **Content Sharing:** Posts, stories, and short-form videos (loops)
- **Social Interaction:** Following, likes, comments, and engagement metrics
- **Real-time Communication:** Instant messaging with online presence
- **User Discovery:** Suggested users and search functionality
- **Notifications:** Real-time alerts for interactions and engagements

### User Types & Roles

#### 1. **Authenticated Users**
- Users who have signed up and logged into the platform
- Have access to all platform features
- Can create, edit, and delete their own content
- Can interact with other users' content

#### 2. **Anonymous Users**
- Users who access the platform without authentication
- Limited access to public features
- Redirected to login for creating content or interactions

### Core Principles
- **User-Centric Design:** Focus on intuitive user interactions
- **Real-time Responsiveness:** WebSocket-driven real-time updates
- **Scalability:** Modular architecture for horizontal scaling
- **Security:** End-to-end authentication and authorization

---

## Architecture Overview

### 3-Tier Architecture Pattern

```
┌─────────────────────────────────────────────────────────┐
│                   PRESENTATION LAYER                     │
│                 (React + Vite Frontend)                  │
│  - UI Components  - State Management  - User Interface   │
└────────────────────┬────────────────────────────────────┘
                     │ HTTP/WebSocket
┌────────────────────▼────────────────────────────────────┐
│                  BUSINESS LOGIC LAYER                    │
│            (Node.js + Express Backend API)              │
│  - Controllers  - Routes  - Middleware  - Services      │
└────────────────────┬────────────────────────────────────┘
                     │ Native MongoDB Queries
┌────────────────────▼────────────────────────────────────┐
│                    DATA LAYER                            │
│            (MongoDB + Cloudinary Storage)               │
│  - Database  - Collections  - Media Storage             │
└─────────────────────────────────────────────────────────┘
```

### Key Separation of Concerns

| Layer | Responsibility | Technologies |
|-------|-----------------|--------------|
| **Presentation** | UI rendering, state management, user interactions | React 19, Vite, Redux Toolkit, Tailwind CSS |
| **Business Logic** | Request handling, business rules, data validation | Node.js, Express 5, Socket.io |
| **Data** | Data persistence, media storage | MongoDB, Cloudinary |

---

## Technology Stack

### Frontend Technologies
| Technology | Purpose | Version |
|-----------|---------|---------|
| **React** | UI framework and component library | 19.1.0 |
| **Vite** | Build tool and development server | 7.0.0 |
| **Redux Toolkit** | State management and data flow | 2.8.2 |
| **React Router** | Client-side routing and navigation | 7.6.3 |
| **Tailwind CSS** | Utility-first CSS framework | 4.1.11 |
| **Axios** | HTTP client for API calls | 1.10.0 |
| **Socket.io Client** | WebSocket client for real-time communication | 4.8.1 |
| **React Icons** | Icon library | 5.5.0 |
| **React Spinners** | Loading indicators | 0.17.0 |

### Backend Technologies
| Technology | Purpose | Version |
|-----------|---------|---------|
| **Node.js** | JavaScript runtime for server-side execution | LTS |
| **Express** | Web framework for REST API development | 5.1.0 |
| **MongoDB** | NoSQL document database | Latest |
| **Mongoose** | MongoDB object modeling | 8.16.1 |
| **Socket.io** | Real-time bidirectional communication | 4.8.1 |
| **JWT (jsonwebtoken)** | Token-based authentication | 9.0.2 |
| **bcryptjs** | Password hashing and encryption | 3.0.2 |
| **Cloudinary** | Cloud media storage and CDN | 2.7.0 |
| **Nodemailer** | Email service for password reset | 7.0.4 |
| **Multer** | File upload middleware | 2.0.1 |
| **CORS** | Cross-Origin Resource Sharing | 2.8.5 |
| **dotenv** | Environment variable management | 17.0.0 |
| **Nodemon** | Development tool for auto-reloading | 3.1.10 |

### Infrastructure & External Services
- **Cloudinary:** Cloud-based media storage and CDN
- **Email Service:** Nodemailer for SMTP-based email delivery
- **MongoDB Atlas:** Managed MongoDB cloud database
- **Vercel:** Frontend deployment platform
- **Heroku/Railway:** Backend deployment platform

---

## System Components

### Frontend Components Structure

```
frontend/src/
├── components/
│   ├── Feed.jsx                 # Main feed display component
│   ├── Post.jsx                 # Individual post component
│   ├── LoopCard.jsx             # Short video card component
│   ├── StoryCard.jsx            # Story display component
│   ├── StoryDp.jsx              # Story profile picture
│   ├── NotificationCard.jsx     # Notification item
│   ├── Nav.jsx                  # Navigation bar
│   ├── LeftHome.jsx             # Left sidebar navigation
│   ├── RightHome.jsx            # Right sidebar user suggestions
│   ├── FollowButton.jsx         # Follow/Unfollow button
│   ├── OtherUser.jsx            # Other user profile view
│   ├── OnlineUser.jsx           # Online user indicator
│   ├── Messages/
│   │   ├── SenderMessage.jsx    # Sent message bubble
│   │   ├── ReceiverMessage.jsx  # Received message bubble
│   │   └── MessageArea.jsx      # Chat interface
│   └── VideoPlayer.jsx          # Video playback component
├── pages/
│   ├── SignUp.jsx               # User registration
│   ├── SignIn.jsx               # User login
│   ├── Home.jsx                 # Main feed page
│   ├── Profile.jsx              # User profile page
│   ├── EditProfile.jsx          # Profile editing
│   ├── Upload.jsx               # Content upload
│   ├── Messages.jsx             # Messaging hub
│   ├── MessageArea.jsx          # Individual chat
│   ├── Notifications.jsx        # Notification center
│   ├── Loops.jsx                # Short videos feed
│   ├── Story.jsx                # Story viewing
│   ├── Search.jsx               # User search
│   └── ForgotPassword.jsx       # Password recovery
├── hooks/
│   ├── getAllPost.jsx           # Fetch posts hook
│   ├── getAllLoops.jsx          # Fetch loops hook
│   ├── getAllStories.jsx        # Fetch stories hook
│   ├── getAllNotifications.jsx # Fetch notifications
│   ├── getCurrentUser.jsx       # Fetch current user
│   ├── getFollowingList.jsx    # Fetch following list
│   ├── getPrevChatUsers.jsx    # Fetch chat history
│   └── getSuggestedUsers.jsx   # Fetch user suggestions
├── redux/
│   ├── store.js                 # Redux store configuration
│   ├── userSlice.js             # User state slice
│   ├── postSlice.js             # Posts state slice
│   ├── loopSlice.js             # Loops state slice
│   ├── storySlice.js            # Stories state slice
│   ├── messageSlice.js          # Messages state slice
│   └── socketSlice.js           # Socket connection state
└── assets/                      # Static assets and images
```

### Backend Components Structure

```
backend/
├── config/
│   ├── db.js                    # MongoDB connection
│   ├── cloudinary.js            # Cloudinary configuration
│   ├── Mail.js                  # Email service setup
│   └── token.js                 # JWT token utilities
├── controllers/
│   ├── auth.controllers.js      # Authentication logic
│   ├── user.controllers.js      # User management
│   ├── post.controllers.js      # Post operations
│   ├── loop.controllers.js      # Loop/reel operations
│   ├── story.controllers.js     # Story operations
│   └── message.controllers.js   # Messaging logic
├── models/
│   ├── user.model.js            # User schema
│   ├── post.model.js            # Post schema
│   ├── loop.model.js            # Loop schema
│   ├── story.model.js           # Story schema
│   ├── message.model.js         # Message schema
│   ├── conversation.model.js    # Conversation schema
│   └── notification.model.js    # Notification schema
├── routes/
│   ├── auth.routes.js           # Authentication endpoints
│   ├── user.routes.js           # User endpoints
│   ├── post.routes.js           # Post endpoints
│   ├── loop.routes.js           # Loop endpoints
│   ├── story.routes.js          # Story endpoints
│   └── message.routes.js        # Message endpoints
├── middlewares/
│   ├── isAuth.js                # Authentication middleware
│   └── multer.js                # File upload configuration
├── socket.js                    # Socket.io event handlers
├── index.js                     # Express server setup
└── public/                      # Static files
```

---

## Data Models & Entity Relationships

### User Model
```javascript
{
  _id: ObjectId,
  name: String,
  userName: String (unique),
  email: String (unique),
  password: String (hashed with bcrypt),
  profileImage: String (Cloudinary URL),
  coverImage: String (Cloudinary URL),
  bio: String,
  gender: String,
  followers: [ObjectId], // Array of user IDs
  following: [ObjectId], // Array of user IDs
  posts: [ObjectId], // Array of post IDs
  loops: [ObjectId], // Array of loop IDs
  stories: [ObjectId], // Array of story IDs
  saved: [ObjectId], // Array of saved post IDs
  notifications: [ObjectId], // Array of notification IDs
  createdAt: Date,
  updatedAt: Date
}
```

### Post Model
```javascript
{
  _id: ObjectId,
  author: ObjectId, // Reference to User
  content: String, // Caption
  image: String, // Cloudinary URL
  video: String, // Cloudinary URL
  likes: [ObjectId], // Array of user IDs who liked
  comments: [{
    _id: ObjectId,
    author: ObjectId, // Reference to User
    text: String,
    createdAt: Date
  }],
  savedBy: [ObjectId], // Array of users who saved
  createdAt: Date,
  updatedAt: Date
}
```

### Story Model
```javascript
{
  _id: ObjectId,
  author: ObjectId, // Reference to User
  media: String, // Cloudinary URL (image or video)
  viewers: [ObjectId], // Array of user IDs who viewed
  expiresAt: Date, // Auto-delete after 24 hours
  createdAt: Date
}
```

### Loop Model
```javascript
{
  _id: ObjectId,
  author: ObjectId, // Reference to User
  video: String, // Cloudinary URL
  caption: String,
  likes: [ObjectId], // Array of user IDs who liked
  comments: [{
    _id: ObjectId,
    author: ObjectId, // Reference to User
    text: String,
    createdAt: Date
  }],
  createdAt: Date,
  updatedAt: Date
}
```

### Message Model
```javascript
{
  _id: ObjectId,
  conversationId: ObjectId, // Reference to Conversation
  sender: ObjectId, // Reference to User
  content: String,
  image: String, // Optional image attachment
  createdAt: Date
}
```

### Conversation Model
```javascript
{
  _id: ObjectId,
  participants: [ObjectId], // Array of 2 user IDs
  messages: [ObjectId], // Array of message IDs
  lastMessage: String,
  lastMessageTime: Date,
  updatedAt: Date
}
```

### Notification Model
```javascript
{
  _id: ObjectId,
  recipient: ObjectId, // Reference to User
  sender: ObjectId, // Reference to User
  type: String, // 'like', 'comment', 'follow', 'message'
  content: String,
  link: ObjectId, // Reference to post/story/loop (if applicable)
  isRead: Boolean,
  createdAt: Date
}
```

### Entity Relationship Diagram

```
┌─────────────────────┐
│       USER          │
├─────────────────────┤
│ _id (PK)            │
│ name                │
│ email (unique)      │
│ password            │
│ profileImage        │
│ followers []        │
│ following []        │
│ saved []            │
└────────┬────────────┘
         │
    ┌────┴────────────────┬─────────────┬────────────┐
    │                     │             │            │
    ▼                     ▼             ▼            ▼
┌────────┐            ┌────────┐  ┌────────┐  ┌──────────┐
│ POST   │            │ LOOP   │  │ STORY  │  │CONVERSATION│
├────────┤            ├────────┤  ├────────┤  ├──────────┤
│ _id(PK)│            │_id(PK) │  │_id(PK)│  │_id(PK)   │
│author□ │            │author□ │  │author□ │  │partic.[] │
│content │            │video   │  │media   │  │messages[]│
│likes[] │            │caption │  │viewers │  └──────────┘
│comments│            │likes[] │  │expires │       │
│savedBy[]            │comments            │       ▼
└────────┘            └────────┘  └────────┘  ┌──────────┐
                                               │ MESSAGE  │
                                               ├──────────┤
                                               │_id(PK)   │
                                               │conv.id□  │
                                               │sender□   │
                                               │content   │
                                               └──────────┘

Legend: 
□ = Foreign Key Reference
[] = Array Reference
PK = Primary Key
```

---

## Key Workflows & Features

### 1. Authentication Workflow

```
START
  │
  ├─► SIGN UP REQUEST
  │   ├─ Validate input (email format, password strength)
  │   ├─ Check if user exists
  │   ├─ Hash password with bcryptjs
  │   ├─ Create user document in MongoDB
  │   └─ Generate JWT token
  │
  ├─► SIGN IN REQUEST
  │   ├─ Find user by email
  │   ├─ Compare password hash
  │   ├─ Generate JWT token
  │   └─ Return token + user data
  │
  ├─► FORGOT PASSWORD REQUEST
  │   ├─ Find user by email
  │   ├─ Generate OTP token
  │   ├─ Send OTP via Nodemailer
  │   └─ Store OTP in session/temporary DB
  │
  └─► RESET PASSWORD
      ├─ Verify OTP
      ├─ Hash new password
      ├─ Update user document
      └─ Send confirmation email
```

### 2. Post Creation & Sharing Workflow

```
START
  │
  ├─► USER UPLOADS CONTENT
  │   ├─ Select image/video file
  │   ├─ Add caption (optional)
  │   └─ Click POST button
  │
  ├─► MEDIA UPLOAD
  │   ├─ Send file to Multer (validate file type/size)
  │   ├─ Upload to Cloudinary
  │   └─ Receive Cloudinary URL
  │
  ├─► CREATE POST DOCUMENT
  │   ├─ Create post in MongoDB
  │   ├─ Store author ID, media URL, caption
  │   ├─ Add to user's posts array
  │   └─ Trigger notification to followers
  │
  ├─► FEED DISTRIBUTION
  │   ├─ Query followers' following lists
  │   ├─ Add post to their feed
  │   └─ Update in real-time via Socket.io
  │
  └─► ENGAGEMENT
      ├─ Users can like/unlike post
      ├─ Users can comment
      ├─ Users can save/bookmark
      └─ Post owner receives notifications
```

### 3. Real-time Messaging Workflow

```
START
  │
  ├─► USER OPENS MESSAGE
  │   ├─ Check if conversation exists
  │   ├─ Fetch message history
  │   └─ Display sorted by timestamp
  │
  ├─► USER TYPES & SENDS MESSAGE
  │   ├─ Message saved to MongoDB
  │   ├─ Emit Socket.io event (message:new)
  │   ├─ Broadcast to recipient in real-time
  │   └─ Update conversation lastMessage
  │
  ├─► RECIPIENT RECEIVES
  │   ├─ Socket.io listener receives event
  │   ├─ UI updates immediately
  │   ├─ Message appears in chat
  │   └─ Create notification
  │
  ├─► ONLINE STATUS
  │   ├─ User connects via Socket.io
  │   ├─ Emit "user:online" event
  │   ├─ Broadcast to all connected users
  │   ├─ Update online users list
  │   └─ When disconnects, emit "user:offline"
  │
  └─► IMAGE SHARING
      ├─ Upload image to Cloudinary
      ├─ Create message with image URL
      └─ Send like text message
```

### 4. Story Workflow

```
START
  │
  ├─► CREATE STORY
  │   ├─ Upload image/video
  │   ├─ Upload to Cloudinary
  │   ├─ Create story document (24h TTL)
  │   ├─ Add to user's stories array
  │   └─ Add to followers' story feed
  │
  ├─► VIEW STORY
  │   ├─ Click on user's story DP
  │   ├─ Load story media
  │   ├─ Display auto-advance timer
  │   ├─ Add viewer ID to story viewers array
  │   └─ Move to next story on timer
  │
  ├─► TRACK VIEWERS
  │   ├─ Maintain viewers array in story
  │   ├─ Allow user to see who viewed
  │   └─ Calculate engagement metrics
  │
  └─► AUTO-EXPIRY
      ├─ TTL index on createdAt field
      ├─ MongoDB auto-deletes after 24h
      └─ No manual cleanup needed
```

### 5. Follow/Unfollow Workflow

```
START
  │
  ├─► USER CLICKS FOLLOW
  │   ├─ Add targetUser ID to user.following[]
  │   ├─ Add user ID to targetUser.followers[]
  │   ├─ Create FOLLOW notification
  │   ├─ Emit Socket.io event
  │   └─ Update UI in real-time
  │
  ├─► USER CLICKS UNFOLLOW
  │   ├─ Remove targetUser ID from user.following[]
  │   ├─ Remove user ID from targetUser.followers[]
  │   ├─ Remove related notifications
  │   ├─ Emit Socket.io event
  │   └─ Update UI in real-time
  │
  └─► NOTIFICATIONS
      ├─ Create notification for followed user
      ├─ Broadcast notification via Socket.io
      ├─ Mark as unread initially
      └─ User can dismiss or interact
```

---

## Real-time Communication Architecture

### Socket.io Implementation

#### Connection Flow
```
CLIENT                          SERVER
  │                              │
  ├─ io.connect()  ──────────►  Socket listener
  │                              │
  │                        ├─ Authenticate user
  │                        ├─ Link socket ID to user ID
  │                        ├─ Add to online users set
  │                        └─ Broadcast "user:online"
  │
  ◄──────── "user:online"  ┤
  │                        │
  │                    (Connection established)
```

#### Key Socket Events

| Event | Direction | Purpose | Payload |
|-------|-----------|---------|---------|
| `connection` | Server | User connects to socket | Socket ID |
| `user:online` | Server → Clients | Broadcast online status | `{ userId, timestamp }` |
| `user:offline` | Server → Clients | Broadcast offline status | `{ userId, timestamp }` |
| `message:new` | Client → Server → Clients | New message sent | `{ senderId, conversationId, content, timestamp }` |
| `message:typing` | Client → Server → Clients | User typing indicator | `{ userId, conversationId }` |
| `notification:new` | Server → Clients | New notification | `{ type, sender, content, timestamp }` |
| `post:like` | Client → Server → Clients | Post liked | `{ postId, userId }` |
| `post:comment` | Client → Server → Clients | Comment added | `{ postId, userId, comment }` |
| `follow:new` | Client → Server → Clients | New follow | `{ followerId, followeeId }` |
| `disconnect` | Server | User disconnects | Socket ID |

### Socket.io Architecture Diagram

```
┌─────────────────────────────────────────────┐
│          Frontend (React + Socket.io)        │
├─────────────────────────────────────────────┤
│ - Connect on auth                           │
│ - Emit events on user actions               │
│ - Listen for server broadcasts              │
│ - Update Redux state on events              │
└────────────────────┬────────────────────────┘
                     │
              WebSocket Connection
              (TCP Upgrade w/ Polling)
                     │
┌────────────────────▼────────────────────────┐
│      Backend (Node.js + Socket.io)         │
├─────────────────────────────────────────────┤
│ socket.js                                   │
│ - Connection/Disconnection handlers        │
│ - Event listeners & processors             │
│ - Broadcasting to rooms/namespaces         │
│ - Real-time data updates to MongoDB        │
└─────────────────────────────────────────────┘
```

### Rooms & Namespaces

```
/                          # Default namespace
├── messages:conv_{id}     # Private conversation room
├── notifications:user_{id} # User notification room
└── online:users           # Global online users room

User Socket.io Flow:
1. Join "online:users" on connect
2. Join "messages:conv_{id}" when opening chat
3. Join "notifications:user_{id}" on auth
4. Leave rooms on disconnect
```

---

## API Architecture

### RESTful API Design

#### Base URL
```
Development:  http://localhost:8000/api
Production:   https://api.vybe-platform.com/api
```

#### Request/Response Pattern

```
REQUEST:
POST /api/endpoint
Headers:
  - Content-Type: application/json
  - Authorization: Bearer {JWT_TOKEN}
Body:
  {
    "field1": "value1",
    "field2": "value2"
  }

RESPONSE (Success):
{
  "success": true,
  "message": "Operation successful",
  "data": {
    ...resource data
  }
}

RESPONSE (Error):
{
  "success": false,
  "message": "Error description",
  "error": "error_code"
}
```

### API Endpoints Overview

#### Authentication Routes (`/auth`)
- `POST /auth/signup` - User registration
- `POST /auth/signin` - User login
- `POST /auth/forgot-password` - Initiate password reset
- `POST /auth/reset-password` - Complete password reset
- `POST /auth/logout` - User logout

#### User Routes (`/user`)
- `GET /user/profile/:userId` - Get user profile
- `PUT /user/profile/edit` - Update user profile
- `GET /user/suggested` - Get suggested users
- `POST /user/:userId/follow` - Follow user
- `POST /user/:userId/unfollow` - Unfollow user
- `GET /user/:userId/followers` - Get followers list
- `GET /user/:userId/following` - Get following list

#### Post Routes (`/post`)
- `POST /post/create` - Create new post
- `GET /post/feed` - Get user's feed
- `GET /post/:postId` - Get single post
- `PUT /post/:postId/edit` - Edit post
- `DELETE /post/:postId` - Delete post
- `POST /post/:postId/like` - Like post
- `POST /post/:postId/unlike` - Unlike post
- `POST /post/:postId/comment` - Add comment
- `POST /post/:postId/save` - Save post

#### Loop Routes (`/loop`)
- `POST /loop/create` - Create short video
- `GET /loop/feed` - Get loops feed
- `GET /loop/:loopId` - Get single loop
- `DELETE /loop/:loopId` - Delete loop
- `POST /loop/:loopId/like` - Like loop
- `POST /loop/:loopId/unlike` - Unlike loop
- `POST /loop/:loopId/comment` - Comment on loop

#### Story Routes (`/story`)
- `POST /story/create` - Create story
- `GET /story/feed` - Get stories feed
- `GET /story/:storyId` - Get single story
- `DELETE /story/:storyId` - Delete story
- `POST /story/:storyId/view` - Mark as viewed

#### Message Routes (`/message`)
- `POST /message/send` - Send message
- `GET /message/conversations` - Get all conversations
- `GET /message/conversation/:conversationId` - Get messages in conversation
- `GET /message/search/:userName` - Search users for messaging

#### Notification Routes (via Socket.io primarily)
- Real-time notifications delivered via WebSocket
- Fallback HTTP endpoints available

### Middleware Pipeline

```
REQUEST
  │
  ├─► CORS Middleware
  │   └─ Validate origin, methods
  │
  ├─► Body Parser Middleware
  │   └─ Parse JSON/multipart data
  │
  ├─► Cookie Parser Middleware
  │   └─ Extract JWT from cookies/headers
  │
  ├─► Authentication Middleware (isAuth)
  │   ├─ Verify JWT token
  │   ├─ Extract user ID
  │   ├─ Attach user to request object
  │   └─ On failure: return 401 Unauthorized
  │
  ├─► Multer Middleware (for file uploads)
  │   ├─ Validate file type
  │   ├─ Validate file size
  │   ├─ Store temporarily
  │   └─ Pass to controller
  │
  ├─► Rate Limiting (optional)
  │   └─ Prevent abuse
  │
  └─► Route Handler (Controller)
      └─ Business logic execution

RESPONSE
  │
  ├─► Format response
  ├─► Set status code
  ├─► Send response
  └─► Return to client
```

---

## Security Architecture

### Authentication & Authorization

#### JWT Token Flow

```
1. USER SIGNUP/SIGNIN
   ├─ Server verifies credentials
   ├─ Generates JWT: jwt.sign({ userId, email }, SECRET, { expiresIn: '7d' })
   ├─ Sends token to client
   └─ Client stores in localStorage/sessionStorage

2. AUTHENTICATED REQUESTS
   ├─ Client includes: Authorization: Bearer {JWT_TOKEN}
   ├─ Server middleware verifies token
   ├─ Token valid: Proceed with request
   └─ Token invalid/expired: Return 401 Unauthorized

3. TOKEN REFRESH
   ├─ Token expires after 7 days
   ├─ User must sign in again (or implement refresh tokens)
   └─ New token issued
```

#### Password Security

- **Hashing Algorithm:** bcryptjs (salting + hashing)
- **Salt Rounds:** 10 (default)
- **Storage:** Hashed passwords only stored in DB
- **Transmission:** HTTPS only (in production)

### Data Protection

#### Sensitive Data Handling

| Data | Protection Method |
|------|-------------------|
| Passwords | Bcryptjs hashing with salt |
| Email | Hashed in login attempts |
| JWT Tokens | Signed with secret, expiration |
| Messages | Transmitted over HTTPS/WSS |
| Media Files | Stored on Cloudinary (CDN) |

#### Input Validation & Sanitization

- Email format validation
- Password strength requirements
- File type validation (on server)
- Input length limits
- SQL injection prevention (MongoDB queries)
- XSS prevention (React auto-escaping)

### Authorization Rules

```
User Profile:
├─ Can view: Anyone (public profile)
├─ Can edit: Only profile owner
└─ Can delete: Only profile owner

Posts:
├─ Can view: Anyone (if public)
├─ Can create: Authenticated users
├─ Can edit: Only post author
├─ Can delete: Only post author
└─ Can like: Any authenticated user

Messages:
├─ Can send: Authenticated users
├─ Can view: Only conversation participants
├─ Can delete: Sender only (after some time limit)
└─ Can forward: Not allowed

Stories:
├─ Can view: Followers only (if private)
├─ Can view: Anyone (if public)
├─ Can create: Authenticated users
├─ Can delete: Only story owner
└─ Auto-delete: After 24 hours
```

### CORS Configuration

```javascript
corsOptions = {
  origin: ['https://vybe-frontend.vercel.app', 'http://localhost:5173'],
  methods: ['GET', 'POST', 'PUT', 'DELETE', 'PATCH'],
  credentials: true,
  allowedHeaders: ['Content-Type', 'Authorization']
}
```

---

## Scalability & Performance

### Database Indexing Strategy

```javascript
// User Collection
db.users.createIndex({ email: 1 }, { unique: true });
db.users.createIndex({ userName: 1 }, { unique: true });
db.users.createIndex({ createdAt: -1 });
db.users.createIndex({ followers: 1 });
db.users.createIndex({ following: 1 });

// Post Collection
db.posts.createIndex({ author: 1, createdAt: -1 });
db.posts.createIndex({ likes: 1 });
db.posts.createIndex({ createdAt: -1 });
db.posts.createIndex({ 'comments.author': 1 });

// Story Collection
db.stories.createIndex({ author: 1 });
db.stories.createIndex({ expiresAt: 1 }, { expireAfterSeconds: 86400 });

// Message Collection
db.messages.createIndex({ conversationId: 1, createdAt: -1 });
db.messages.createIndex({ sender: 1 });

// Conversation Collection
db.conversations.createIndex({ participants: 1 });
db.conversations.createIndex({ updatedAt: -1 });
```

### Caching Strategy

#### Client-Side Caching
- **Redux State:** In-memory cache for current session
- **LocalStorage:** Persist auth tokens and user preferences
- **Browser Cache:** Static assets (images, CSS, JS)

#### Server-Side Caching (Future Enhancement)
- **Redis Cache:** For frequently accessed data
  - Online users list
  - Popular posts
  - User follower counts
  - Suggested users

```
Cache Invalidation Strategy:
├─ Time-based: Expire cache every 5-10 minutes
├─ Event-based: Invalidate on post/follow/message creation
├─ User-based: Different cache per user
└─ Tag-based: Group related cache entries
```

### Query Optimization

#### Pagination Implementation
```javascript
// Posts per page
db.posts
  .find({ author: { $in: followingList } })
  .sort({ createdAt: -1 })
  .skip((page - 1) * limit)
  .limit(limit);
```

#### Lazy Loading
- Load initial 10 posts on page load
- Load 5 more posts on scroll
- Implement infinite scroll pattern

#### Population/Joins (Mongoose)
```javascript
// Fetch post with author details
Post.findById(postId)
  .populate('author', 'name userName profileImage')
  .populate('comments.author', 'name userName profileImage');
```

### Performance Metrics

| Metric | Target | Tool |
|--------|--------|------|
| Page Load Time | < 2s | Vite + Code Splitting |
| API Response Time | < 200ms | Express optimization |
| Time to Interactive | < 3s | React lazy loading |
| Largest Contentful Paint | < 2.5s | Image optimization |
| Cumulative Layout Shift | < 0.1 | CSS optimization |

### Scalability Plan

#### Horizontal Scaling
```
Current Architecture (Single Instance):
┌─────────────────────────────────────┐
│     Frontend (Vercel)               │
│     ├─ Auto-scales with traffic     │
│     └─ CDN globally distributed     │
└──────────────┬──────────────────────┘
               │
      ┌────────▼─────────┐
      │  Backend (1 node)│
      │  - Express       │
      │  - Socket.io     │
      └────────┬─────────┘
               │
      ┌────────▼─────────┐
      │    MongoDB       │
      │   Atlas (shared) │
      └──────────────────┘

Future Scaling (Multiple Backends):
┌─────────────────────────────────────┐
│     Load Balancer (Nginx)           │
├─────────────────────────────────────┤
│ Backend Node 1 │ Backend Node 2 │ 3 │
│   Express 1    │   Express 2    │ 3 │
│  Socket.io 1   │  Socket.io 2   │ 3 │
└────────┬───────┴─────────┬──────┴───┘
         │                 │
    ┌────▼─────────────────▼────┐
    │   Redis (Socket.io Adapter)
    │   (Session & event broadcast)
    └────┬──────────────────────┘
         │
    ┌────▼──────────────┐
    │  MongoDB Cluster  │
    │  (Replicated DB)  │
    └───────────────────┘
```

#### Vertical Scaling
- Increase server RAM and CPU
- Upgrade MongoDB instance size
- Optimize queries and indexes

#### Database Optimization
- Sharding strategy based on userId
- Archiving old data to cold storage
- Replicate critical collections

---

## Deployment Architecture

### Frontend Deployment (Vercel)

```
Development Branch
  │
  ├─► git push (dev branch)
  │
  └─► Vercel CI/CD
      ├─ Build: npm run build
      ├─ Test: npm run lint
      ├─ Deploy to preview
      └─ Auto URL generated

Production Branch (Main)
  │
  ├─► Code review & merge to main
  │
  └─► Vercel CI/CD
      ├─ Build: npm run build (optimized)
      ├─ Deploy to production
      ├─ CDN distribution
      └─ HTTPS certificate
```

### Backend Deployment (Railway/Heroku)

```
Push to Repository
  │
  └─► CI/CD Pipeline
      ├─ Clone repository
      ├─ Install dependencies
      ├─ Run tests (if configured)
      ├─ Build application
      ├─ Set environment variables
      ├─ Start server: node index.js
      └─ Assign public URL

Environment Variables (.env):
├─ MONGODB_URI - Database connection
├─ CLOUDINARY_KEY - Media upload keys
├─ JWT_SECRET - Token signing key
├─ SMTP_USER - Email credentials
├─ FRONTEND_URL - CORS origin
├─ NODE_ENV - Environment type
└─ PORT - Server port
```

### Environment Differences

| Environment | Database | Frontend URL | API URL |
|-------------|----------|-------------|---------|
| **Development** | MongoDB Local | localhost:5173 | localhost:8000 |
| **Staging** | MongoDB Atlas | staging.vybe.com | api-staging.vybe.com |
| **Production** | MongoDB Atlas | vybe.com | api.vybe.com |

### Database Backup Strategy

```
MongoDB Atlas Automatic Backups:
├─ Snapshots every 6 hours
├─ Retention: 35 days
├─ Restore capability: Point-in-time
├─ Backup location: AWS/Azure (configured)
└─ Encryption: AES-256 encryption

Manual Backups:
├─ Daily export of critical collections
├─ Store in secure cloud storage
└─ Version control backup manifests
```

---

## Error Handling & Monitoring

### Error Handling Strategy

#### Client-Side Error Handling
```javascript
try {
  const response = await api.post('/post/create', formData);
  dispatch(addPost(response.data));
} catch (error) {
  if (error.response?.status === 401) {
    // Token expired, redirect to login
  } else if (error.response?.status === 413) {
    // File too large
    showError('File size exceeds 5MB limit');
  } else {
    // Generic error
    showError(error.response?.data?.message || 'An error occurred');
  }
}
```

#### Server-Side Error Handling
```javascript
app.use((err, req, res, next) => {
  console.error(err);
  
  if (err.name === 'ValidationError') {
    res.status(400).json({ success: false, message: 'Validation failed' });
  } else if (err.name === 'CastError') {
    res.status(400).json({ success: false, message: 'Invalid ID format' });
  } else if (err.status === 401) {
    res.status(401).json({ success: false, message: 'Unauthorized' });
  } else {
    res.status(500).json({ success: false, message: 'Server error' });
  }
});
```

### HTTP Status Codes

| Code | Meaning | Use Case |
|------|---------|----------|
| 200 | OK | Successful request |
| 201 | Created | Resource created |
| 400 | Bad Request | Invalid input |
| 401 | Unauthorized | Auth required/failed |
| 403 | Forbidden | Insufficient permissions |
| 404 | Not Found | Resource doesn't exist |
| 409 | Conflict | Duplicate resource |
| 413 | Payload Too Large | File too large |
| 429 | Too Many Requests | Rate limit exceeded |
| 500 | Server Error | Unexpected error |

### Logging Strategy

```
Log Levels:
├─ DEBUG: Detailed dev info (not in production)
├─ INFO: General operational info
├─ WARN: Warning conditions
├─ ERROR: Error conditions
└─ FATAL: Fatal error conditions

Log Format:
[TIMESTAMP] [LEVEL] [SERVICE] [USER_ID] - MESSAGE

Example:
[2026-04-24T10:30:15.234Z] [INFO] [auth-service] [user_123] - User logged in
[2026-04-24T10:30:20.456Z] [ERROR] [post-service] [user_456] - Failed to upload media: Cloudinary error
```

### Monitoring & Alerts

#### Key Metrics to Monitor
- API response times (average, p95, p99)
- Error rate (5xx errors)
- Database query performance
- Memory usage (backend server)
- Network bandwidth
- Active user connections (Socket.io)
- Message queue length (if using queues)

#### Alert Thresholds
- 5xx Error Rate > 1%
- API Response Time > 1s (average)
- Database Connection Pool > 90% utilization
- Server Memory > 80% utilization
- Socket.io Connections < expected (possible crash)

---

## Future Enhancements

### Phase 2 Features

#### 1. **Direct Messaging Improvements**
- Group chats support
- Message reactions/emojis
- Message editing and deletion
- Read receipts
- Typing indicators with cooldown
- Voice messages

#### 2. **Content Discovery**
- Advanced search with filters
- Hashtag system and trending topics
- Content recommendations (ML-based)
- Explore/Discover page algorithm
- Saved collections/bookmarks

#### 3. **Social Features**
- User blocks and mutes
- Retweet/reshare functionality
- Mentions and tagging
- User verification system
- Badges and achievements

#### 4. **Notifications Enhancements**
- Push notifications (Service Worker)
- Email digest summaries
- Customizable notification preferences
- Do not disturb settings
- Notification history

#### 5. **Content Moderation**
- User reporting system
- Content flagging
- Automated content filtering (spam/NSFW)
- Moderation dashboard
- Appeal system

### Phase 3 - Scalability & Business

#### 1. **Monetization Features**
- Ads integration
- Premium subscription tier
- In-app purchases
- Creator fund/revenue sharing
- Sponsored content

#### 2. **Analytics & Insights**
- Post analytics dashboard
- User engagement metrics
- Growth tracking
- Traffic sources
- Audience demographics

#### 3. **Advanced Security**
- Two-factor authentication (2FA)
- Session management
- IP whitelisting
- Security audit logs
- Encryption at rest

#### 4. **Performance Optimization**
- Redis caching layer
- Database query optimization
- CDN for media delivery
- Lazy loading for all content
- Service worker for offline support

#### 5. **Internationalization**
- Multi-language support
- Localization for UI
- Currency conversion
- Regional content preferences

### Technology Upgrades

```
Current Stack → Future Stack

Frontend:
├─ React 19 → React 20+ / Next.js (SSR)
├─ Vite → Turbopack (faster builds)
├─ Redux → Zustand (lighter state)
└─ Socket.io → WebSocket API (native)

Backend:
├─ Express → Fastify (faster)
├─ Socket.io → WebSocket library
├─ MongoDB → PostgreSQL + MongoDB (hybrid)
└─ Add: GraphQL API, gRPC

Infrastructure:
├─ Add: Redis caching
├─ Add: Elasticsearch (search)
├─ Add: Message queue (RabbitMQ/Kafka)
├─ Add: Load balancer (Nginx)
└─ Add: Monitoring (Prometheus, Grafana)
```

---

## Architecture Diagram (Complete System)

```
┌─────────────────────────────────────────────────────────────┐
│                         CLIENTS                              │
│  ┌──────────────────┐         ┌──────────────────────────┐  │
│  │ Web Browser      │         │ Mobile App (Future)      │  │
│  │ (React + Vite)   │         │ (React Native/Flutter)   │  │
│  └────────┬─────────┘         └────────────┬─────────────┘  │
└───────────┼────────────────────────────────┼────────────────┘
            │                                │
    ┌───────▼────────┐              ┌───────▼────────┐
    │ HTTPS/WSS      │              │ HTTPS/WSS      │
    │ REST API       │              │ REST API       │
    │ WebSocket      │              │ WebSocket      │
    └────────┬───────┘              └────────┬───────┘
             │                               │
    ┌────────▼───────────────────────────────▼─────────┐
    │         API GATEWAY / LOAD BALANCER              │
    │  (Nginx / AWS ALB)                               │
    └────────┬───────────────────────────────┬─────────┘
             │                               │
    ┌────────▼────────────┐  ┌──────────────▼────────┐
    │ Backend Server 1    │  │ Backend Server 2      │
    │ - Express.js        │  │ - Express.js          │
    │ - Socket.io         │  │ - Socket.io           │
    │ - Controllers       │  │ - Controllers         │
    │ - Middleware        │  │ - Middleware          │
    └────────┬────────────┘  └──────────────┬────────┘
             │                               │
             └────────────┬──────────────────┘
                          │
        ┌─────────────────┼─────────────────┐
        │                 │                 │
    ┌───▼────┐    ┌──────▼────┐    ┌──────▼──────┐
    │ MongoDB │    │ Cloudinary│    │   Redis     │
    │ Database│    │   Storage │    │   Cache     │
    │ (Atlas) │    │    CDN    │    │  (Future)   │
    └─────────┘    └───────────┘    └─────────────┘

Legend:
- MongoDB Atlas: Main data persistence
- Cloudinary: Media storage and CDN
- Redis: Distributed caching (future)
```

---

## Summary

VYBE is architected as a modern, scalable social media platform with clear separation of concerns across three layers. The use of real-time WebSocket technology combined with RESTful APIs provides both responsiveness and flexibility. The modular design allows for easy feature additions and scaling.

### Key Architectural Highlights

✅ **Separation of Concerns** - Clear division between presentation, logic, and data  
✅ **Real-time Features** - WebSocket integration for instant updates  
✅ **Scalability** - Designed for horizontal and vertical scaling  
✅ **Security** - JWT authentication, password hashing, input validation  
✅ **Performance** - Pagination, lazy loading, query optimization  
✅ **Maintainability** - Modular structure with clear naming conventions  
✅ **Cloud-Native** - Cloud storage and managed databases  

### Next Steps for Development

1. Implement comprehensive error logging and monitoring
2. Add Redis caching layer for performance
3. Implement rate limiting for API endpoints
4. Add comprehensive unit and integration tests
5. Set up CI/CD pipeline with automated testing
6. Implement advanced search functionality
7. Add content recommendation engine
8. Implement two-factor authentication

---

**Document Prepared By:** Development Team  
**Last Review Date:** April 24, 2026  
**Next Review Date:** Q3 2026
