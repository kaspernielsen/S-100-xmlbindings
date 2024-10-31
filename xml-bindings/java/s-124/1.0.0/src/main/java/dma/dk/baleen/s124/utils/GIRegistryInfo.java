package dma.dk.baleen.s124.utils;

import _int.iho.s100.catalog._5_0.S100CompliancyCategory;
import _int.iho.s100.catalog._5_0.S100ProductSpecification;

import java.math.BigInteger;
import java.time.LocalDate;

/**
 * The IHO GI Registry Information Class.
 * </p>
 * This class contains hard coded information on the product specification used to generate this package.
 * <p/>
 * This class must be updated in every change of the S-100 or the data produce specification.
 */
public class GIRegistryInfo {

    /** The Data Product Name as per the IHO GI Registry. */
    public static final String DATA_PRODUCT_NAME = "Navigational Warnings";

    /** The Data Product Identifier as per the IHO GI Registry. */
    public static final String DATA_PRODUCT_IDENTIFIER = "S-124";

    /** The Data Product Number as per the IHO GI Registry. */
    public static final Integer DATA_PRODUCT_NUMBER = 666;

    /** The Data Product Version as per the IHO GI Registry. */
    public static final String DATA_PRODUCT_VERSION = "1.0.0";

    /** The Data Product Version as per the IHO GI Registry. */
    public static final S100CompliancyCategory DATA_PRODUCT_COMPLIANCY_CATEGORY = S100CompliancyCategory.CATEGORY_1;

    /** The Data Product Date as per the IHO GI Registry. */
    public static final LocalDate DATA_PRODUCT_DATE = LocalDate.of(2023, 4, 27);

    /** {@return the S-100 data product specification for this library} */
    public static S100ProductSpecification getProductSpecification() {
        S100ProductSpecification productSpecification = new S100ProductSpecification();
        productSpecification.setName(DATA_PRODUCT_NAME);
        productSpecification.setProductIdentifier(DATA_PRODUCT_IDENTIFIER);
        productSpecification.setNumber(BigInteger.valueOf(DATA_PRODUCT_NUMBER));
        productSpecification.setVersion(DATA_PRODUCT_VERSION);
        productSpecification.setCompliancyCategory(DATA_PRODUCT_COMPLIANCY_CATEGORY);
        productSpecification.setDate(DATA_PRODUCT_DATE);
        return productSpecification;
    }
}
