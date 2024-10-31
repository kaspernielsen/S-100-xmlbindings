package dma.dk.baleen.s124.utils;

import static java.util.Objects.requireNonNull;

import java.io.IOException;
import java.io.OutputStream;
import java.net.URL;
import java.util.ArrayList;
import java.util.List;

import javax.xml.XMLConstants;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;

import org.xml.sax.ErrorHandler;
import org.xml.sax.SAXException;
import org.xml.sax.SAXParseException;

import jakarta.xml.bind.JAXBContext;
import jakarta.xml.bind.JAXBElement;
import jakarta.xml.bind.JAXBException;
import jakarta.xml.bind.Marshaller;
import jakarta.xml.bind.util.JAXBSource;

public class S124GmlValidator {

    private static final Schema SCHEMA;
    
    static {
        SchemaFactory schemaFactory = SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
        try {
            URL schemaResource = S124GmlValidator.class.getResource("/xsd/S-124.xsd");
            SCHEMA = schemaFactory.newSchema(schemaResource);
        } catch (SAXException e) {
            throw new RuntimeException(e);
        }
    }

    private Validator createAndConfigureValidator(List<ValidationError> validationErrors) {
        Validator validator = SCHEMA.newValidator();

        validator.setErrorHandler(new ErrorHandler() {
            @Override
            public void error(SAXParseException e) {
                validationErrors.add(new ValidationError("ERROR", e.getMessage(), e.getLineNumber(), e.getColumnNumber()));
            }

            @Override
            public void fatalError(SAXParseException e) {
                validationErrors.add(new ValidationError("FATAL", e.getMessage(), e.getLineNumber(), e.getColumnNumber()));
            }

            @Override
            public void warning(SAXParseException e) {
                validationErrors.add(new ValidationError("WARNING", e.getMessage(), e.getLineNumber(), e.getColumnNumber()));
            }
        });
        return validator;
    }

    public void printXml(JAXBElement<?> jaxbElement, OutputStream out) throws JAXBException {
        JAXBContext jaxbContext = JAXBContext.newInstance(jaxbElement.getValue().getClass());
        Marshaller marshaller = jaxbContext.createMarshaller();
        marshaller.setProperty(Marshaller.JAXB_FORMATTED_OUTPUT, true);
        marshaller.marshal(jaxbElement, out);
    }

    public List<ValidationError> validateAgainstSchema(JAXBElement<?> jaxbElement) throws JAXBException {
        requireNonNull(jaxbElement);

        JAXBContext jaxbContext = JAXBContext.newInstance(jaxbElement.getValue().getClass());
        JAXBSource source = new JAXBSource(jaxbContext, jaxbElement);

        List<ValidationError> validationErrors = new ArrayList<>();

        try {
            Validator validator = createAndConfigureValidator(validationErrors);
            validator.validate(source);
        } catch (SAXException e) {
            validationErrors.add(new ValidationError("UNKNOWN", e.getMessage(), null, null));
        } catch (IOException e) {
            validationErrors.add(new ValidationError("IO", e.getMessage(), null, null));
        }

        return validationErrors;
    }

    public record ValidationError(String type, String message, Integer lineNumber, Integer columnNumber) {}
}
