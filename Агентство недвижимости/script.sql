USE [master]
GO
/****** Object:  Database [EstateAgency]    Script Date: 25.01.2025 18:27:44 ******/
CREATE DATABASE [EstateAgency]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'EstateAgency', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\EstateAgency.mdf' , SIZE = 8192KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'EstateAgency_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL15.SQLEXPRESS\MSSQL\DATA\EstateAgency_log.ldf' , SIZE = 8192KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT
GO
ALTER DATABASE [EstateAgency] SET COMPATIBILITY_LEVEL = 150
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [EstateAgency].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [EstateAgency] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [EstateAgency] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [EstateAgency] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [EstateAgency] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [EstateAgency] SET ARITHABORT OFF 
GO
ALTER DATABASE [EstateAgency] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [EstateAgency] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [EstateAgency] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [EstateAgency] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [EstateAgency] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [EstateAgency] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [EstateAgency] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [EstateAgency] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [EstateAgency] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [EstateAgency] SET  DISABLE_BROKER 
GO
ALTER DATABASE [EstateAgency] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [EstateAgency] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [EstateAgency] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [EstateAgency] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [EstateAgency] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [EstateAgency] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [EstateAgency] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [EstateAgency] SET RECOVERY SIMPLE 
GO
ALTER DATABASE [EstateAgency] SET  MULTI_USER 
GO
ALTER DATABASE [EstateAgency] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [EstateAgency] SET DB_CHAINING OFF 
GO
ALTER DATABASE [EstateAgency] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [EstateAgency] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [EstateAgency] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [EstateAgency] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
ALTER DATABASE [EstateAgency] SET QUERY_STORE = OFF
GO
USE [EstateAgency]
GO
/****** Object:  Table [dbo].[Auth]    Script Date: 25.01.2025 18:27:44 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Auth](
	[Login] [nvarchar](50) NOT NULL,
	[Password] [nvarchar](20) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Buyer]    Script Date: 25.01.2025 18:27:44 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Buyer](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[FIO] [nvarchar](200) NOT NULL,
	[Price_range] [nvarchar](50) NOT NULL,
	[Wishes] [nvarchar](max) NOT NULL,
	[Date_of_application] [date] NOT NULL,
	[Telephone] [nvarchar](12) NOT NULL,
 CONSTRAINT [PK_Buyer] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Realty]    Script Date: 25.01.2025 18:27:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Realty](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Price] [int] NOT NULL,
	[Address] [nvarchar](150) NOT NULL,
	[Square] [decimal](8, 2) NOT NULL,
	[Type] [nvarchar](50) NOT NULL,
	[Specifications] [nvarchar](max) NOT NULL,
 CONSTRAINT [PK_Realty] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Report]    Script Date: 25.01.2025 18:27:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Report](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[ID_Buyer] [int] NOT NULL,
	[ID_Seller] [int] NOT NULL,
	[ID_Realty] [int] NOT NULL,
	[Date] [date] NOT NULL,
	[Price] [nvarchar](9) NOT NULL,
 CONSTRAINT [PK_Report] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Seller]    Script Date: 25.01.2025 18:27:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Seller](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[FIO] [nvarchar](200) NOT NULL,
	[Desired_Price] [int] NOT NULL,
	[Telephone] [nvarchar](12) NOT NULL,
	[ID_Realty] [int] NOT NULL,
 CONSTRAINT [PK_Seller] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[Tasks]    Script Date: 25.01.2025 18:27:45 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Tasks](
	[ID] [int] IDENTITY(1,1) NOT NULL,
	[Tasks] [nvarchar](50) NOT NULL,
	[Deskription] [nvarchar](max) NOT NULL,
	[Date] [datetime] NOT NULL,
	[Place] [nvarchar](200) NOT NULL,
	[Opponent] [nvarchar](200) NOT NULL,
 CONSTRAINT [PK_Tasks] PRIMARY KEY CLUSTERED 
(
	[ID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
ALTER TABLE [dbo].[Report]  WITH CHECK ADD  CONSTRAINT [FK_Report_Buyer] FOREIGN KEY([ID_Buyer])
REFERENCES [dbo].[Buyer] ([ID])
GO
ALTER TABLE [dbo].[Report] CHECK CONSTRAINT [FK_Report_Buyer]
GO
ALTER TABLE [dbo].[Report]  WITH CHECK ADD  CONSTRAINT [FK_Report_Realty] FOREIGN KEY([ID_Realty])
REFERENCES [dbo].[Realty] ([ID])
GO
ALTER TABLE [dbo].[Report] CHECK CONSTRAINT [FK_Report_Realty]
GO
ALTER TABLE [dbo].[Report]  WITH CHECK ADD  CONSTRAINT [FK_Report_Seller] FOREIGN KEY([ID_Seller])
REFERENCES [dbo].[Seller] ([ID])
GO
ALTER TABLE [dbo].[Report] CHECK CONSTRAINT [FK_Report_Seller]
GO
ALTER TABLE [dbo].[Seller]  WITH CHECK ADD  CONSTRAINT [FK_Seller_Realty] FOREIGN KEY([ID_Realty])
REFERENCES [dbo].[Realty] ([ID])
GO
ALTER TABLE [dbo].[Seller] CHECK CONSTRAINT [FK_Seller_Realty]
GO
USE [master]
GO
ALTER DATABASE [EstateAgency] SET  READ_WRITE 
GO
