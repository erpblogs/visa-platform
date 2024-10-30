# Visa Service Management

## Overview
This module extends Odoo's product module to manage visa services. It adds specific fields and features needed for visa service management.

## Features
### Extended Product Fields
1. **Service Requirements (service_requirement_ids)**
   - Manages list of requirements for each visa service
   - Examples: passport copies, financial documents, photos
   - Tracks mandatory and optional requirements

2. **Process Steps (service_process_ids)**
   - Defines the processing steps for each visa service
   - Tracks duration and responsible parties
   - Helps in monitoring service progress

3. **Duration Fields**
   - **Estimated Duration (estimated_duration)**
     - Number of days typically needed to process the visa
     - Used for planning and setting customer expectations
   - **Validity Period (validity_period)**
     - How long the visa remains valid (in months)
     - Important for service description and pricing

4. **Entry Type (entry_type)**
   - Single Entry: One-time entry permission
   - Multiple Entry: Multiple entries allowed during validity period
   - Affects pricing and service requirements

## Usage Examples
### Tourist Visa Service