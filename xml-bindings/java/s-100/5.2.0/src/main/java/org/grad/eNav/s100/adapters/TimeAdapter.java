/*
 * Copyright (c) 2024 GLA Research and Development Directorate
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package org.grad.eNav.s100.adapters;

import jakarta.xml.bind.annotation.adapters.XmlAdapter;

import java.time.LocalTime;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeFormatterBuilder;

/**
 * The Time Adapter Class.
 *
 * This is used to translate between the java.time.LocalTime objects and the XML
 * time elements.
 *
 * @author Nikolaos Vastardis (email: Nikolaos.Vastardis@gla-rad.org)
 */
public class TimeAdapter extends XmlAdapter<String, LocalTime> {

    public static final String S100_TIME_FORMAT = "HHmmss";
    public final DateTimeFormatter S100_TIME_FORMATTER = new DateTimeFormatterBuilder()
            .parseCaseInsensitive()
            .appendPattern(S100_TIME_FORMAT)
            .parseStrict()
            .toFormatter();

    /**
     * Marshall a Java Date object into an XML element.
     *
     * @param date      The java Date object
     * @return The XML element
     */
    @Override
    public String marshal(LocalTime date) {
        synchronized (S100_TIME_FORMATTER) {
            return S100_TIME_FORMATTER.format(date);
        }
    }

    /**
     * Unmarshall an XML element into a Java Date object.
     *
     * @param xml       The XML element
     * @return The Java Date object
     */
    @Override
    public LocalTime unmarshal(String xml) {
        synchronized (S100_TIME_FORMATTER) {
            return LocalTime.parse(xml, S100_TIME_FORMATTER);
        }
    }

}