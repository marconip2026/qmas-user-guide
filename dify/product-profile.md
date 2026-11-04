# Product Management — Every Tab of the Product Profile

After you create a product, its profile holds everything about it. This guide explains each tab in the profile's left menu and the import option on the product list.

- **Module:** Product Management
- **Open a profile:** https://qmas.icw.io/product/list → click a product
- **Tabs:** Document · Shipping Detail · Compliance Data · Quality Requirement · AI Risk Screening · CPSC eFiling · Packaging Detail
- **See also:** Create and edit a product: https://marconip2026.github.io/qmas-user-guide/product-management/
- **Checked against:** QMAS dev, 4 Nov 2026
- **Full guide with screenshots:** https://marconip2026.github.io/qmas-user-guide/product-profile/

## Overview

1. **Document**: upload, organise, share and set reminders for the product's files.
2. **Shipping Detail**: sizes, weights and barcodes for the selling unit and cartons.
3. **Compliance Data**: record test results, certificates and other compliance data.
4. **Quality Requirement**: list the product's quality requirements, use templates and send them to testing or document review.
5. **AI Risk Screening**: run AI compliance screenings for this product.
6. **CPSC eFiling**: submit eFiling for this product and see its eFiling log.
7. **Packaging Detail**: record each packaging component, its materials and suppliers.

## Step-by-step

### 1. Document

Shows every file linked to the product. Use **New Folder** to organise files and **Upload** to add a file (see the Document Management guide for the upload pop-up). Filter by **Type**, **Source** or **Checked**, switch between **All** and **Archived**, and search with **Search Files**.

![Document tab.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/01-document.jpg)

Tick one or more files to open the toolbar:

| Action | What it does |
|---|---|
| Set Data | Add compliance data (test, certificate or other) from this file. |
| Set Dates & Reminder | Set issue, expiry and review dates and an email reminder. |
| Archive | Move the file to the Archived tab. |
| Download | Download the file. |
| Share | Create a share link with an expiry period. Copy it or send it by email. |
| Rename / Edit Type | Change the file name or document type. |
| Move | Move the file to a folder. |
| Remove | Remove the file. |

![Toolbar after selecting a file.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/02-document-toolbar.jpg)

![Share Via Link — choose how long the link stays valid, then Copy or By Email.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/03-document-share.jpg)


### 2. Shipping Detail

Shows the length, width, height, gross and net weight, quantity and barcode for the **Selling Unit**, **Inner Carton** and **Outer Carton**. To change them, click **⋮** next to the product name → **Edit product** and update **Shipping Information**.

![Shipping Detail tab.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/04-shipping-detail.jpg)


### 3. Compliance Data

Three sections: **Test Data**, **Certificate Data** and **Other**. Click **Add Data** (or **Add** once a section has records).

![Compliance Data tab before any data is added.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/05-compliance-data.jpg)

**Test Data** records one test result:

- **Result** (required): Passed, Failed or Report As Is.
- **Export Market** (required). For US eFiling, choose **United States (CPSC eFiling submission)**.
- **Legislation, Test Item & Citation** (required): type a keyword such as “lead” and pick the test item.
- **Report ID**, **Issue Party** (required), **Expiry Date** and **Test Date / Report Date**.
- Link the report under **Existing Product Document** (a file already on the product) or **New Document**.

![Search legislation and test items by keyword.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/07-test-item-search.jpg)

![A completed Test Data record with the report linked.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/08-test-data-filled.jpg)

Click **Confirm**. The record appears in the Test Data table with its export market, legislation, test item, citation, report ID and issue party.

![Saved test data.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/09-test-data-saved.jpg)

**Certificate Data** works the same way. Fill in the certificate **Type**, **Issue Party**, **Score / Overall Rating**, **Expiry Date** and **Certificate Date**, then link the certificate file.

![Certificate Data form.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/10-certificate-data-form.jpg)


### 4. Quality Requirement

Quality Requirement lists what the product must meet, for example test standards or packaging rules. Each requirement has a **Type** (the group) and a **Name**. You can attach compliance data to it as proof, mark it completed, and reuse the list in Product Testing or Document Review. The tick next to the title turns green when the requirements are completed.

![Empty Quality Requirement tab: Add Requirement, Test Plan (AI) and the ⋯ menu.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/11-quality-requirement.jpg)

**4a. Add a requirement yourself**

- Click **Add Requirement** (or **Add** at the top right once the list has items).
- **Type**: pick an existing type, or type a new one and choose **+ Create “…”**.
- **Name**: pick an existing name for that type, or type a new one and choose **+ Create**. Picking a different Type clears the Name.
- Tick **Mandatory** if the requirement must be met, then click **Confirm**.

![Add Requirement with Type, Name and Mandatory.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/19-requirement-filled.jpg)

**4b. Add requirements from a template (fastest)**

Click **⋯** next to the title → **Templates**:

| Option | What it does |
|---|---|
| Apply Template | Pick a saved template (use **View** to preview it) and click **Apply**. All its requirements are added. |
| Save As Template | Save this product's requirements as a template for other products. |
| Manage Templates | Edit or delete your templates. |

![⋯ → Templates.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/20-templates-menu.jpg)

![Apply Template — View or Apply a saved template.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/21-apply-template.jpg)

QMAS shows “<template name> applied”. Requirements are grouped by Type; the number next to the Type is how many requirements it has.

![Requirements after applying a template.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/22-requirement-list.jpg)

**4c. Attach proof and complete a requirement**

- Click **+** on a requirement to open **Attach Compliance Data**. Choose the **Test Data**, **Certificate Data** or **Other** tab, tick the records and click **Confirm**. If a record you just added is missing, click **Reload Data**. To add new data, go to Compliance Data first.
- Click **⌄** to expand a requirement and see the attached data. Click the bin icon to detach it.
- Click **⋯** on a requirement for **Edit**, **Duplicate**, **Upload Document**, **Mark As Completed** and **Remove**.
- **Mark As Completed** shows “Requirement Completed” and turns the requirement’s tick green.

![Attach Compliance Data — tick the test record.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/23-attach-compliance.jpg)

![The attached test data under the requirement.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/24-requirement-attached.jpg)

![⋯ menu on one requirement.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/25-requirement-row-menu.jpg)

![Requirement marked as completed.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/26-requirement-completed.jpg)

**4d. Send requirements to a job**

- **⋯ → Import To Product Testing**: tick the requirements (or **Select All**) and click **Confirm to Create Job**. Product Testing → Request Quotations opens with this product added, and the requirements appear under **Quality Requirement** in step 2.
- **⋯ → Import to Document Review** → **Create Job** or **Create Job for supplier**: starts a Document Review job with these requirements.
- **⋯ → Export As Document**: exports the requirement list as a document.

![Import To Product Testing — choose requirements, then Confirm to Create Job.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/29-import-to-pt.jpg)

![The requirement carried into Product Testing step 2.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/31-pt-requirement-carried.jpg)

![Import to Document Review → Create Job or Create Job for supplier.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/28-import-doc-review.jpg)

**4e. Test Plan (AI)**

Click **Test Plan** to let AI suggest a test plan. Fill in the **Product Description** (more detail gives better results), **Import Country** and **Product Intended Used By**, upload up to 6 product images, then click **Generate Test Plan**.

![Test Plan pop-up.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/27-test-plan.jpg)


### 5. AI Risk Screening

Lists the AI screenings for this product. Click **Add** to start one. The pop-up and results are explained in the AI Insight guide: https://marconip2026.github.io/qmas-user-guide/ai-insight/

![AI Risk Screening tab.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/17-ai-risk-screening.jpg)


### 6. CPSC eFiling

Shows the **eFiling Log** for this product. Click **Submit eFiling** to create an eFiling. Before you can sync with CPSC, add your API Key and Secret Key in **Company Profile** (link in the grey note). The full flow is in the eFiling guide: https://marconip2026.github.io/qmas-user-guide/efiling/

![CPSC eFiling tab.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/16-cpsc-efiling.jpg)


### 7. Packaging Detail

Lists the packaging components of the product. Click **Create Packaging Component** and fill in:

- **Basic Information**: name and description (required), identification no., function, legal role, weight, material type and name, status (Active, Inactive or Draft), and packaging images.
- **Dimension**, **Additional Information**, **Supplier Linkage** and **Technical Documentation** (expand each section).

Click **Confirm**. Use the **Status** filter to show active, inactive or draft components.

![Packaging Details tab.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/14-packaging.jpg)

![Create Packaging Component.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/15-packaging-component.jpg)


### 8. Import products in bulk

On the Product Management list, click **Import Product**. Download the ICW Product template (**download here**), fill it in, upload the Excel file (one file at a time), then click **Next**. Only the ICW template can be used.

![Import Product.](https://marconip2026.github.io/qmas-user-guide/product-profile/img/18-import-product.jpg)

## Tips

- **Hide product details** at the top right hides the product card on the left.
- Link test reports to Test Data. eFiling can reuse this data when you quick-select test data.
- Use requirement **Templates** so similar products get the same requirements.

## FAQ

**Q: How do I add a test result to a product?**
A: Open the product → Compliance Data → Test Data → Add Data. Fill in Result, Export Market, Legislation/Test Item, Issue Party, link the report, then Confirm.

**Q: How do I share a product document?**
A: Open the product → Document, tick the file, click Share, choose the link expiry, then Copy or By Email.

**Q: How do I add quality requirements to a product?**
A: Open the product → Quality Requirement → Add Requirement, or ⋯ → Templates to apply a saved template.

**Q: Where do I record packaging information?**
A: Open the product → Packaging Detail → Create Packaging Component.

**Q: How do I import many products?**
A: On Product Management, click Import Product, download the ICW template, fill it in and upload it.

**Q: How do I reuse quality requirements for many products?**
A: Open a product → Quality Requirement → ⋯ → Templates → Save As Template. On other products use ⋯ → Templates → Apply Template.

**Q: How do I prove a requirement is met?**
A: On the requirement click +, attach the test or certificate data, then ⋯ → Mark As Completed.

